import subprocess
import sys

def get_current_version():
    result = subprocess.run(
        ["bump-my-version", "show", "current_version", "--config-file", ".bumpversion.toml"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()

def get_git_diff():
    result = subprocess.run(
        ["git", "diff", "--cached", "pyproject.toml"],
        capture_output=True,
        text=True,
    )
    return result.stdout

def main():
    current_version = get_current_version()
    diff = get_git_diff()

    if current_version in diff:
        print("✅ Version has been bumped.")
        return 0
    else:
        print("❌ ERROR: Version not bumped in pyproject.toml.")
        print("Please run:")
        print("  bump-my-version bump patch  # or minor/major")
        return 1

if __name__ == "__main__":
    sys.exit(main())
