from gendiff.logic.diff import generate_diff

def test_generate_diff():
    with open('tests/fixtures/answer1.txt', 'r') as output_file:
        answer1 = output_file.read()
    assert generate_diff('tests/fixtures/test_generate_fixture1.json', 'tests/fixtures/test_generate_fixture2.json') == answer1
    with open('tests/fixtures/answer2.txt', 'r') as output_file:
        answer2 = output_file.read()
    assert generate_diff('tests/fixtures/test_generate_fixture3.yaml', 'tests/fixtures/test_generate_fixture4.yml') == answer2
    with open('tests/fixtures/answer3.txt', 'r') as output_file:
        answer3 = output_file.read()
    assert generate_diff('tests/fixtures/test_generate_fixture5.json', 'tests/fixtures/test_generate_fixture6.json') == answer3
    assert generate_diff('tests/fixtures/test_generate_fixture7.yaml', 'tests/fixtures/test_generate_fixture8.yaml') == answer3