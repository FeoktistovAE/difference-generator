from gendiff import generate_diff
import pytest
from tests import FIXTURE_PATH


def build_path(file_name):
    return FIXTURE_PATH + file_name


@pytest.mark.parametrize(
    "test_input_file1, test_input_file2, format, answer_file_name",
    [
        ('test_generate_fixture1.json', 'test_generate_fixture4.yml', 'json', 'json_answer.txt'),
        ('test_generate_fixture3.yaml', 'test_generate_fixture4.yml', 'plain', 'plain_answer.txt'),
        ('test_generate_fixture1.json', 'test_generate_fixture2.json', 'stylish', 'stylish_answer.txt')
    ]
)
def test_generate_diff(test_input_file1, test_input_file2, format, answer_file_name):
    with open(build_path(answer_file_name)) as output_file:
        expected = output_file.read()
    assert generate_diff(build_path(test_input_file1), build_path(test_input_file2), format) == expected
