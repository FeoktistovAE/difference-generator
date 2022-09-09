from gendiff.diff import generate_diff
import pytest


JSON_ANSWER = 'tests/fixtures/json_answer.txt'
PLAIN_ANSWER = 'tests/fixtures/plain_answer.txt' 
STYLISH_ANSWER = 'tests/fixtures/stylish_answer.txt'
JSON_FIXTURE1 = 'tests/fixtures/test_generate_fixture1.json'
JSON_FIXTURE2 = 'tests/fixtures/test_generate_fixture2.json'
YAML_FIXTURE3 = 'tests/fixtures/test_generate_fixture3.yaml'
YML_FIXTURE4 = 'tests/fixtures/test_generate_fixture4.yml'
JSON_FORMAT = 'json'
PLAIN_FORMAT = 'plain'
STYLISH_FORMAT = 'stylish'


with open(JSON_ANSWER, 'r') as output_file:
    answer_json = output_file.read()
with open(PLAIN_ANSWER, 'r') as output_file:
    answer_plain = output_file.read()
with open(STYLISH_ANSWER, 'r') as output_file:
    answer_stylish = output_file.read()
    

@pytest.mark.parametrize(
    "test_input_file1, test_input_file2, format, expected", 
    [(JSON_FIXTURE1, YML_FIXTURE4, JSON_FORMAT, answer_json),
    (YAML_FIXTURE3, YML_FIXTURE4, PLAIN_FORMAT, answer_plain),
    (JSON_FIXTURE1, JSON_FIXTURE2, STYLISH_FORMAT, answer_stylish)]
)
def test_generate_diff(test_input_file1, test_input_file2, format, expected):
    assert generate_diff(test_input_file1, test_input_file2, format) == expected
