#!/usr/bin/env python


from gendiff.cli import parse
from gendiff import generate_diff


def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
