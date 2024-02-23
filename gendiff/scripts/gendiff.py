#!/usr/bin/env python3

from gendiff import cli
from gendiff import generate_diff


def main():
    *args, format = cli()
    dif = generate_diff(args, format)
    print(dif)


if __name__ == "__main__":
    main()
