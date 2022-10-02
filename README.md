### Hexlet tests and linter status:
[![Actions Status](https://github.com/FeoktistovAE/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/FeoktistovAE/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8ac0337820229d3a6e16/maintainability)](https://codeclimate.com/github/FeoktistovAE/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8ac0337820229d3a6e16/test_coverage)](https://codeclimate.com/github/FeoktistovAE/python-project-lvl2/test_coverage)
[![make-tests](https://github.com/FeoktistovAE/python-project-lvl2/actions/workflows/hexlet-tests.yml/badge.svg)](https://github.com/FeoktistovAE/python-project-lvl2/actions/workflows/hexlet-tests.yml)
### Description:
    This package provides CLI utilitte that compares two configuration files and shows a difference.
    CLI utilitte supports YAML and JSON formatts and also provides visualisation of found differences
    in three different views: stylish, plain and json. 
    You can select one of them, using the -f flag as demonstrated below.
    The project was written as a part of the Hexlet training course by student Feoktistov Andrei.
    This project was built using python3.8, poetry and flake8 tools for bash.
### Package installation:
```bash
pip3 install git+https://github.com/FeoktistovAE/python-project-lvl2
```

```bash
make setup
```
### Utility usage:
```bash
gendiff -h
```

```bash
usage: gendiff [-h] [-f FORMAT] first_file second_file
```
[![asciicast](https://asciinema.org/a/si25r82LfnKhXpD4kuVvApGrE.svg)](https://asciinema.org/a/si25r82LfnKhXpD4kuVvApGrE)
-geindiff stylish format work example
[![asciicast](https://asciinema.org/a/G61MjsJjVeweqYGbvMz1MxEYH.svg)](https://asciinema.org/a/G61MjsJjVeweqYGbvMz1MxEYH)
-gendiff plain format work example
[![asciicast](https://asciinema.org/a/zFu0FMW5PSuTsQn6HDzfZcYN1.svg)](https://asciinema.org/a/zFu0FMW5PSuTsQn6HDzfZcYN1)
-gendiff json format work example