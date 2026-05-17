#!/usr/bin/env python3
"""
Validate YAML frontmatter in all project files.
Required fields: title, category, status, summary.
Skips: _template.md, README.md
"""
import sys
from pathlib import Path
import frontmatter

REQUIRED_FIELDS = ["title", "category", "status", "summary"]
VALID_CATEGORIES = {"work", "personal"}
VALID_STATUSES = {"idea", "in-progress", "complete", "paused", "archived"}

SKIP_PATTERNS = {"_template.md", "README.md"}

errors = []

project_files = [
    p for p in Path("projects").rglob("*.md")
    if p.name not in SKIP_PATTERNS
]

if not project_files:
    print("No project files found — nothing to validate.")
    sys.exit(0)

for path in sorted(project_files):
    post = frontmatter.load(str(path))
    meta = post.metadata

    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"{path}: missing required field '{field}'")

    category = meta.get("category", "")
    if category and category not in VALID_CATEGORIES:
        errors.append(
            f"{path}: invalid category '{category}' — must be one of {sorted(VALID_CATEGORIES)}"
        )

    status = meta.get("status", "")
    if status and status not in VALID_STATUSES:
        errors.append(
            f"{path}: invalid status '{status}' — must be one of {sorted(VALID_STATUSES)}"
        )

if errors:
    print(f"\n❌ Found {len(errors)} frontmatter error(s):\n")
    for error in errors:
        print(f"  • {error}")
    sys.exit(1)

print(f"✅ Validated {len(project_files)} project file(s) — all frontmatter is valid.")
