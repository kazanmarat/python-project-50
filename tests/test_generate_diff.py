import json
from gendiff import generate_diff


def test_generate_diff():
    path = 'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
    result_file = open('tests/fixtures/test_flat.txt', 'r')
    result = result_file.read()
    result_file.close()
    assert generate_diff(path) == result
