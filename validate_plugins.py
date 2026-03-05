#!/usr/bin/env python3
"""Validate Product OS plugin structure and consistency."""

import json
import sys
from pathlib import Path

REQUIRED_PLUGIN_FIELDS = {"name", "version", "description", "author", "keywords", "license"}
REQUIRED_SKILL_FRONTMATTER = {"name", "description"}

PLUGIN_DIR = "pm-brain"

EXPECTED_COMMANDS = [
    "think.md", "status.md", "brief.md", "plan.md", "update.md",
    "strategy.md", "discover.md", "build.md", "launch.md", "measure.md",
    "log.md",
]

# Agent definition skills can be shorter than knowledge skills
AGENT_SKILLS = {"coordinator", "context-manager", "getting-started",
                "strategist", "discoverer", "executor", "growth", "analyst"}


def parse_frontmatter(filepath: Path) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}

    end = content.find("---", 3)
    if end == -1:
        return {}

    frontmatter = {}
    for line in content[3:end].strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value

    return frontmatter


def validate_marketplace(root: Path, errors: list, warnings: list):
    """Validate marketplace.json."""
    mp = root / ".claude-plugin" / "marketplace.json"
    if not mp.exists():
        errors.append("Missing .claude-plugin/marketplace.json")
        return

    data = json.loads(mp.read_text())

    if data.get("name") != "product-os":
        warnings.append(f"marketplace.json name is '{data.get('name')}', expected 'product-os'")

    plugins = data.get("plugins", [])
    if len(plugins) != 1:
        warnings.append(f"Expected 1 plugin in marketplace, found {len(plugins)}")

    for p in plugins:
        if p.get("name") != PLUGIN_DIR:
            errors.append(f"marketplace.json plugin name '{p.get('name')}' != expected '{PLUGIN_DIR}'")
        source = root / p["source"].lstrip("./")
        if not source.is_dir():
            errors.append(f"Plugin source directory missing: {p['source']}")


def validate_plugin(plugin_dir: Path, errors: list, warnings: list):
    """Validate the plugin."""
    name = plugin_dir.name

    # Check plugin.json
    pj = plugin_dir / ".claude-plugin" / "plugin.json"
    if not pj.exists():
        errors.append(f"{name}: Missing .claude-plugin/plugin.json")
        return

    data = json.loads(pj.read_text())
    missing = REQUIRED_PLUGIN_FIELDS - set(data.keys())
    if missing:
        errors.append(f"{name}: plugin.json missing fields: {missing}")

    if data.get("name") != name:
        errors.append(f"{name}: plugin.json name '{data.get('name')}' != directory name '{name}'")

    # Check skills
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        errors.append(f"{name}: Missing skills/ directory")
        return

    skill_count = 0
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{name}/skills/{skill_dir.name}: Missing SKILL.md")
            continue

        skill_count += 1
        fm = parse_frontmatter(skill_file)
        missing_fm = REQUIRED_SKILL_FRONTMATTER - set(fm.keys())
        if missing_fm:
            errors.append(f"{name}/skills/{skill_dir.name}: SKILL.md missing frontmatter: {missing_fm}")

        if fm.get("name") != skill_dir.name:
            warnings.append(
                f"{name}/skills/{skill_dir.name}: frontmatter name '{fm.get('name')}' != dir name '{skill_dir.name}'"
            )

        # Check content depth (knowledge skills should be substantial)
        content = skill_file.read_text()
        lines = len(content.strip().split("\n"))
        if skill_dir.name not in AGENT_SKILLS and lines < 100:
            warnings.append(f"{name}/skills/{skill_dir.name}: Only {lines} lines (target: 100+)")

    if skill_count < 30:
        errors.append(f"{name}: Only {skill_count} skills found (expected 34)")

    # Check commands
    commands_dir = plugin_dir / "commands"
    if not commands_dir.is_dir():
        errors.append(f"{name}: Missing commands/ directory")
    else:
        found_commands = {f.name for f in commands_dir.glob("*.md")}
        for expected_cmd in EXPECTED_COMMANDS:
            if expected_cmd not in found_commands:
                errors.append(f"{name}: Missing command: {expected_cmd}")

        for cmd_file in sorted(commands_dir.glob("*.md")):
            fm = parse_frontmatter(cmd_file)
            if "description" not in fm:
                errors.append(f"{name}/commands/{cmd_file.name}: Missing 'description' in frontmatter")


def validate_no_bundled_context(root: Path, errors: list, warnings: list):
    """Ensure context files are NOT bundled in the plugin."""
    ctx_dir = root / "context"
    if ctx_dir.is_dir():
        errors.append("context/ directory should NOT exist in the plugin. Context lives in user's .product-os/context/")


def main():
    root = Path(__file__).parent
    errors = []
    warnings = []

    print("Validating Product OS plugin...\n")

    # Validate marketplace
    validate_marketplace(root, errors, warnings)

    # Validate the plugin
    plugin_dir = root / PLUGIN_DIR
    if plugin_dir.is_dir():
        validate_plugin(plugin_dir, errors, warnings)
    else:
        errors.append(f"Missing plugin directory: {PLUGIN_DIR}")

    # Validate no bundled context
    validate_no_bundled_context(root, errors, warnings)

    # Validate CLAUDE.md exists
    if not (root / "CLAUDE.md").exists():
        errors.append("Missing CLAUDE.md")

    # Report
    skills_dir = root / PLUGIN_DIR / "skills"
    commands_dir = root / PLUGIN_DIR / "commands"
    total_skills = sum(1 for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()) if skills_dir.is_dir() else 0
    total_commands = sum(1 for f in commands_dir.glob("*.md")) if commands_dir.is_dir() else 0

    print(f"Plugin: {PLUGIN_DIR}")
    print(f"Skills: {total_skills}")
    print(f"Commands: {total_commands}")
    print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ! {e}")
        print()
        sys.exit(1)
    else:
        print("All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
