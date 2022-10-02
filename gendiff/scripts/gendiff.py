#!/usr/bin/env python


from gendiff.cli import add_args
from gendiff import generate_diff


def main():
    args = add_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
