#!/usr/bin/env python3
import sys

LINE_FIRST = 50
LINE_OTHER = 70

def format_commit(commit_message):
    # clean out double spaces and extra newlines
    commit_words = commit_message.replace("\n", " ").split(" ")
    lines = []
    line_len = LINE_FIRST

    while len(commit_words) > 0:
        line = ""
        while len(commit_words) > 0 and \
               len(line) + len(commit_words[0]) + 1 <= line_len:
            line += f"{commit_words[0]} "
            del commit_words[0]
        line_len = LINE_OTHER
        lines += [line]

    if len(lines) > 1:
        lines.insert(1, "")

    return "\n".join(lines)

def tab_print(string):
    for line in string.split("\n"):
        print(f"\t{line}")

def main(commit_msg_filepath):
    print(f"\nFormatting your commit message to the {LINE_FIRST}-{LINE_OTHER} rule...\n")
    with open(commit_msg_filepath, "r+") as file:
        commit_message = file.read()
        result = format_commit(commit_message)
        tab_print(
            f"New Commit Message:\n{'='*LINE_OTHER}\n{result}\n{'='*LINE_OTHER}\n")
        file.seek(0)
        file.write(result)
        file.close()

if __name__ == "__main__":
    commit_msg_filepath = sys.argv[1]
    main(commit_msg_filepath)
