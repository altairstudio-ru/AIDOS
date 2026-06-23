import subprocess
from datetime import datetime

OUTPUT_FILE = "Docs/TIMELINE.md"

def get_git_log():
    result = subprocess.run(
        ["git", "log", "--pretty=format:%h|%ad|%s", "--date=iso"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split("\n")

def format_entry(line):
    if not line or "|" not in line:
        return None

    parts = line.split("|")
    if len(parts) < 3:
        return None

    commit, date, message = parts[0], parts[1], parts[2]

    return f"- **{date}** `{commit}` — {message}"

def build_timeline():
    log = get_git_log()

    entries = []
    for line in log:
        formatted = format_entry(line)
        if formatted:
            entries.append(formatted)

    content = "# AI Development OS — Timeline\n\n"
    content += "Auto-generated from git history.\n\n"
    content += "\n".join(entries)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Timeline updated → {OUTPUT_FILE}")

if __name__ == "__main__":
    build_timeline()
