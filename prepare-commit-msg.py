#!/usr/bin/env python3
import sys, re
from subprocess import check_output

def format_commit(commit_message, line_first=20, line_other=72):
    # clean out double spaces and extra newlines
    commit_words = commit_message.replace("\n", " ").split(" ")
    lines = []
    line_len = line_first

    while len(commit_words) > 0:
        line = ""
        while len(commit_words) > 0 and \
               len(line) + len(commit_words[0]) + 1 <= line_len:
            line += f" {commit_words[0]}"
            del commit_words[0]
        line_len = line_other
        lines += [line]

    if len(lines) > 1:
        lines.insert(1, "")

    return "\n".join(lines)

def main(commit_msg_filepath):
    print("\nFormatting your commit message to the 50-70 rule...")
    with open(commit_msg_filepath, "r+") as file:
        commit_message = file.read()
        result = format_commit(commit_message)
        print(f"New Commit Message:\n{'='*30}\n{result}\n{'='*30}")
        file.write(result)
        file.close()

if __name__ == "__main__":
    pass
    commit_msg_filepath = sys.argv[1]
    main(commit_msg_filepath)
