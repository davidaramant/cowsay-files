#!/usr/bin/python
import sys
from pathlib import Path

def escape_line(line):
    line = line.replace("\\", "\\\\")
    line = line.replace("@", "\\@")
    line = line.replace("%", "\\%")
    line = line.replace("$", "\\$")
    return line

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def main():
    input_file = sys.argv[1]
    cow_file = Path(input_file).stem + ".cow"
    print(f"Creating {cow_file}...")

    with open(cow_file, "w") as cow_file:
        cow_file.write('$t = "$thoughts ";\n')
        cow_file.write("$the_cow= <<EOC;\n")
        with open(input_file) as ascii_file:
            for line in nonblank_lines(ascii_file):
                cow_file.write(escape_line(line) + "\n")
        cow_file.write("EOC")

if  __name__ =='__main__':
    main()