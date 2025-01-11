#!/usr/bin/env python

import os

def remove_empty_or_whitespace_first_line(filepath):
    """Removes the first line of a file if it's empty or contains only whitespace.
       Returns True if a line was removed, False otherwise."""
    try:
        with open(filepath, 'r') as f:
            first_line = f.readline()
            if not first_line or first_line.strip() == "":
                # Skip the first line and keep the rest
                rest_of_lines = f.readlines()
                removed_line = True
            else:
              # Keep all the lines
              rest_of_lines = [first_line] + f.readlines()
              removed_line = False

        with open(filepath, 'w') as f:
          f.writelines(rest_of_lines)
        
        return removed_line
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def process_directory(directory):
    """Processes all files in the given directory, printing those where a line was removed."""
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if remove_empty_or_whitespace_first_line(filepath):
                print(f"Removed empty or whitespace first line from: {filepath}")
    print("Finished processing files.")


if __name__ == "__main__":
    public_directory = "public"
    process_directory(public_directory)