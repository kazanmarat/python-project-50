#!/usr/bin/env python3

from gendiff import cli
from gendiff import generate_diff

def main():
    args = cli()
    generate_diff(args)

if __name__ == "__main__":
    main()
