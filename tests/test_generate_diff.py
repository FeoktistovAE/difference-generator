from gendiff import generate_diff
import pytest

FIXTURE_PATH = 'tests/fixtures/'
JSON_FORMAT = 'json'
STYLISH_FORMAT = 'stylish'
PLAIN_FORMAT = 'plain'



def build_path(file_name):
    return FIXTURE_PATH + file_name



with open(build_path('json_answer.txt'), 'r') as output_file:
    answer_json = output_file.read()
with open(build_path('plain_answer.txt'), 'r') as output_file:
    answer_plain = output_file.read()
with open(build_path('stylish_answer.txt'), 'r') as output_file:
    answer_stylish = output_file.read()


@pytest.mark.parametrize(
    "test_input_file1, test_input_file2, format, expected", 
    [(build_path('test_generate_fixture1.json'), build_path('test_generate_fixture4.yml'), JSON_FORMAT, answer_json),
    (build_path('test_generate_fixture3.yaml'), build_path('test_generate_fixture4.yml'), PLAIN_FORMAT, answer_plain),
    (build_path('test_generate_fixture1.json'), build_path('test_generate_fixture2.json'), STYLISH_FORMAT, answer_stylish)]
)
def test_generate_diff(test_input_file1, test_input_file2, format, expected):
    assert generate_diff(test_input_file1, test_input_file2, format) == expected
