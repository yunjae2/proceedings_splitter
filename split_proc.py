#!/usr/bin/python3

import sys
import os
import subprocess


def my_assert(test: bool):
    if not test:
        print(f"usage: {sys.argv[0]} <proceedings> <split level>")
        sys.exit(-1)


def parse_args():
    my_assert(len(sys.argv) == 3)
    return sys.argv[1], sys.argv[2]


def extract_level_info(proc_file, bm_level):
    output = subprocess.check_output(f"pdftk {proc_file} dump_data", shell = True, text=True)
    lines = [x for x in output.splitlines() if x.startswith("Bookmark")]

    meta = []
    lineno = 0
    while lineno < len(lines):
        title_str = lines[lineno+1]
        level_str = lines[lineno+2]
        pgnum_str = lines[lineno+3]

        title = title_str.strip().split()[1]
        level = level_str.strip().split()[1]
        pgnum = pgnum_str.strip().split()[1]

        if level == str(bm_level):
            meta.append((title, pgnum))

        lineno += 4



    return meta


def split_proc(proc_file, meta):
    for idx, (title, start) in enumerate(meta):
        if idx + 1 < len(meta):
            end = meta[idx+1][1]
        else:
            end = ""

        os.system(f"pdftk {proc_file} cat {start}-{end} output test-{title}.pdf")


def main():
    proc_file, bm_level = parse_args()
    meta = extract_level_info(proc_file, bm_level)
    split_proc(proc_file, meta)


if __name__ == "__main__":
    main()
