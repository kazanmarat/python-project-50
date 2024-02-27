#!/usr/bin/env python3

from gendiff import cli
from gendiff import generate_diff


def main():
    file_path1, file_path2, format_name = cli()
    diff = generate_diff(file_path1, file_path2, format_name)
    print(diff)


if __name__ == "__main__":
    main()
