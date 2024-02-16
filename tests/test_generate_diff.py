import pytest
from gendiff import generate_diff

flat_file = open('tests/fixtures/test_flat.txt', 'r')
flat_output = flat_file.read()
flat_file.close()
flat_json = 'tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json'
flat_yml = 'tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml'

flat_cases = [
    (flat_json, flat_output),
    (flat_yml, flat_output),
]


@pytest.mark.parametrize('path, result', flat_cases)
def test_generate_diff(path, result):
    assert generate_diff(path) == result
