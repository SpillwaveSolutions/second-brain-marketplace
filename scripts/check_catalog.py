#!/usr/bin/env python3
"""Catalog checks for the second-brain marketplace.

Two invariants, both of which have already broken in this repo:

  structure -- `marketplace.json` and `.claude-plugin/marketplace.json` are two
  tracked copies of one file. Edit one, forget the other, and the catalog
  disagrees with itself with nothing to notice.

  pins -- every `version` should name the latest published release of its
  source repo. `claude plugin update` resolves the release tag from the repo
  and ignores this field, so a stale pin installs fine and is wrong only where
  the catalog is *read*: fresh-install audits, catalog checks, the README.
  That is why it went unseen. AGER sat two releases behind and worklog five.

Structure runs offline. Pins needs the GitHub API:

    python3 scripts/check_catalog.py            # structure only
    python3 scripts/check_catalog.py --pins     # structure + upstream releases

Unauthenticated GitHub allows 60 requests an hour and this makes one per
plugin, so set GITHUB_TOKEN or GH_TOKEN. A local run borrows `gh auth token`.
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPIES = ("marketplace.json", ".claude-plugin/marketplace.json")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL {msg}")


def check_structure():
    blobs = {}
    for rel in COPIES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            fail(f"{rel} is missing")
            continue
        with open(path, "rb") as fh:
            blobs[rel] = fh.read()

    if len(blobs) == len(COPIES) and len(set(blobs.values())) != 1:
        fail(f"{COPIES[0]} and {COPIES[1]} differ; they must stay byte-identical")

    if COPIES[0] not in blobs:
        return []
    try:
        catalog = json.loads(blobs[COPIES[0]])
    except json.JSONDecodeError as exc:
        fail(f"{COPIES[0]} is not valid JSON: {exc}")
        return []

    if not SEMVER.match(str(catalog.get("metadata", {}).get("version", ""))):
        fail("metadata.version is missing or is not N.N.N")

    plugins = catalog.get("plugins") or []
    if not plugins:
        fail("catalog lists no plugins")
        return []

    seen = set()
    for plugin in plugins:
        name = plugin.get("name")
        if not name:
            fail(f"a plugin entry has no name: {json.dumps(plugin)[:80]}")
            continue
        if name in seen:
            fail(f"{name} is listed more than once")
        seen.add(name)
        if not SEMVER.match(str(plugin.get("version", ""))):
            fail(f"{name} has version {plugin.get('version')!r}, expected N.N.N")
        if not (plugin.get("source") or {}).get("repo"):
            fail(f"{name} has no source.repo")

    print(f"ok   structure: {len(plugins)} plugins, {len(COPIES)} copies checked")
    return plugins


def token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=10
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def latest_release(repo, auth):
    """Latest non-draft, non-prerelease tag, or None. GitHub excludes both."""
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/releases/latest",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "second-brain-marketplace-ci",
            **({"Authorization": f"Bearer {auth}"} if auth else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("tag_name")


def check_pins(plugins):
    auth = token()
    if not auth:
        print("warn pins: no token found, 60 requests/hour applies")

    for plugin in plugins:
        name, repo = plugin["name"], plugin["source"]["repo"]
        pinned = plugin["version"]
        try:
            tag = latest_release(repo, auth)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                fail(f"{name}: {repo} has no published release, pinned at {pinned}")
            else:
                fail(f"{name}: GitHub returned {exc.code} for {repo}")
            continue
        except (urllib.error.URLError, TimeoutError) as exc:
            fail(f"{name}: cannot reach GitHub for {repo}: {exc}")
            continue

        latest = (tag or "").lstrip("v")
        if latest != pinned:
            fail(f"{name}: pinned {pinned}, latest release is {latest or '(untagged)'}")
        else:
            print(f"ok   {name} {pinned}")


def main():
    plugins = check_structure()
    if "--pins" in sys.argv and plugins:
        check_pins(plugins)

    if failures:
        print(f"\n{len(failures)} problem(s) found")
        return 1
    print("\ncatalog is consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
