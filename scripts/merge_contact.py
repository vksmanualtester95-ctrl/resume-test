#!/usr/bin/env python3
"""
merge_contact.py
================
Replaces the <!--PHONE--> and <!--EMAIL--> placeholders in
templates/resume.html with the values from profile/master.local.yaml.

Why this exists:
  The public repo copy of master.yaml has phone/email removed for
  privacy. Locally, those values live in the gitignored
  profile/master.local.yaml. This script merges them into the HTML
  before any export.

Usage (called automatically by check.py / gap.py / Chrome export, or
manually):

  python3 scripts/merge_contact.py

Idempotent — safe to run repeatedly.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HTML = REPO / "templates" / "resume.html"
LOCAL = REPO / "profile" / "master.local.yaml"


def load_local_contact() -> dict:
    """Tiny YAML read — only the contact block, no PyYAML dependency."""
    if not LOCAL.exists():
        print(f"[merge_contact] {LOCAL} not found. Placeholders left in HTML.",
              file=sys.stderr)
        return {}
    contact = {}
    in_contact = False
    for line in LOCAL.read_text().splitlines():
        if line.startswith("contact:"):
            in_contact = True
            continue
        if not in_contact:
            continue
        # Stop at the next top-level key (no leading whitespace) or blank line
        if not line.strip() or (line[0] not in (" ", "\t") and ":" in line):
            break
        # Match:   key: "value with spaces"   or   key: barevalue
        m = re.match(r'^\s+(\w+):\s*"?([^"]*?)"?\s*$', line)
        if m:
            contact[m.group(1)] = m.group(2).strip()
    return contact


def merge() -> int:
    html = HTML.read_text()
    contact = load_local_contact()
    if "<!--PHONE-->" in html and contact.get("phone"):
        html = html.replace("<!--PHONE-->", contact["phone"], 1)
    if "<!--EMAIL-->" in html and contact.get("email"):
        html = html.replace("<!--EMAIL-->", contact["email"], 1)
    HTML.write_text(html)
    remaining = re.findall(r"<!--(PHONE|EMAIL)-->", html)
    if remaining:
        print(f"[merge_contact] WARNING: unresolved placeholders: {remaining}",
              file=sys.stderr)
        return 1
    print("[merge_contact] OK - contact placeholders merged.")
    return 0


if __name__ == "__main__":
    sys.exit(merge())
