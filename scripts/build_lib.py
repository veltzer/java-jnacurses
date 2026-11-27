#!/usr/bin/env python

""" Build the JNA curses shared library, reproducing the Makefile:
gcc -shared -fpic -o libjnacurses.so jnacurses.c -lcurses. File arguments are
ignored; the single source and output are fixed. """

import subprocess
import sys


def main():
    """ main entry point """
    sys.exit(subprocess.call(
        ["gcc", "-Wall", "-Wextra", "-Werror", "-pedantic", "-shared", "-fpic", "-o", "libjnacurses.so",
         "jnacurses.c", "-lcurses"]))


if __name__ == "__main__":
    main()
