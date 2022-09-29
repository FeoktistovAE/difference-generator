from gendiff import generate_diff
import pytest

FIXTURE_PATH = 'tests/fixtures/'


def build_path(file_name):
    return FIXTURE_PATH + file_name


def get_content(file_name):
    with open(file_name, 'r') as output_file:
        content = output_file.read()
    return content


@pytest.mark.parametrize(
    "test_input_file1, test_input_file2, format, expected",
    [
        ('test_generate_fixture1.json', 'test_generate_fixture4.yml', 'json', 'json_answer.txt'),
        ('test_generate_fixture3.yaml', 'test_generate_fixture4.yml', 'plain', 'plain_answer.txt'),
        ('test_generate_fixture1.json', 'test_generate_fixture2.json', 'stylish', 'stylish_answer.txt')
    ]
)
def test_generate_diff(test_input_file1, test_input_file2, format, expected):
    assert generate_diff(build_path(test_input_file1), build_path(test_input_file2), format) == get_content(build_path(expected))
