import os
import re

def rename_md_files():
    # Create 'result' directory if it doesn't exist
    result_dir = 'result'
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # List all files in the current directory
    files = os.listdir()

    # Regular expression pattern to extract date and first two words
    pattern = r'^(\d{4}-\d{2}-\d{2})-(\w+-\w+)-.*\.md$'

    # Counter to track the number prefix
    count = 1

    for filename in files:
        # Check if file is a markdown file
        if filename.endswith('.md'):
            # Extract date and first two words from filename
            match = re.match(pattern, filename)
            if match:
                date, first_two_words = match.groups()

                # Form new filename
                new_filename = f"{date}-{count:02d}-{first_two_words}.md"

                # Rename file and move to 'result' directory
                os.rename(filename, os.path.join(result_dir, new_filename))

                # Increment counter
                count += 1

if __name__ == "__main__":
    rename_md_files()
