import os
import re

REPO_URL = "https://github.com/leegle/ecom-image-prompt-library/tree/main"
TAXONOMY_DIR = os.path.join(os.path.dirname(__file__), "..", "taxonomy")
PATTERN = re.compile(r"`(cases/[^`]+/)`")

def update_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    def replace_match(match):
        folder_path = match.group(1)
        return f"[{folder_path}]({REPO_URL}/{folder_path})"
    
    new_content = PATTERN.sub(replace_match, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def main():
    updated_count = 0
    skipped_count = 0
    
    for filename in sorted(os.listdir(TAXONOMY_DIR)):
        if filename.endswith("-taxonomy-example.md"):
            file_path = os.path.join(TAXONOMY_DIR, filename)
            if update_file(file_path):
                print(f"✓ Updated: {filename}")
                updated_count += 1
            else:
                print(f"✗ Skipped (no changes): {filename}")
                skipped_count += 1
    
    print(f"\nTotal: {updated_count} updated, {skipped_count} skipped")

if __name__ == "__main__":
    main()