# split_proceedings
A command-line tool that splits full proceedings into individual papers based on bookmark information.

## Usage
```bash
$ ./split_proc.py <proceedings> <bookmark level>

# Example
$ ./split_proc.py osdi18_full-proceedings.pdf 1
```
The `<bookmark level>` is commonly 1, however, it is 2 in USENIX ATC'20.
You can find proper value by looking into the bookmarks of the proceedings.
