import pytest
import os
from gendiff import generate_diff


path_fixtures = os.path.join('tests', 'fixtures')


def read_file(path):
    with open(os.path.join(path_fixtures, path)) as file:
        output = file.read()
    return output


file1_json = os.path.join(path_fixtures, 'filepath1.json')
file2_json = os.path.join(path_fixtures, 'filepath2.json')
file1_yml = os.path.join(path_fixtures, 'filepath1.yml')
file2_yml = os.path.join(path_fixtures, 'filepath2.yml')
file3_json = os.path.join(path_fixtures, 'filepath3.json')
file4_json = os.path.join(path_fixtures, 'filepath4.json')
file3_yml = os.path.join(path_fixtures, 'filepath3.yml')
file4_yml = os.path.join(path_fixtures, 'filepath4.yml')


cases = [
    (file1_json, file2_json, 'test_flat.txt', 'stylish'),
    (file1_yml, file2_yml, 'test_flat.txt', 'stylish'),
    (file1_json, file2_yml, 'test_flat.txt', 'stylish'),
    (file3_json, file4_json, 'test_rec.txt', 'stylish'),
    (file3_yml, file4_yml, 'test_rec.txt', 'stylish'),
    (file3_json, file4_json, 'test_plain.txt', 'plain'),
    (file3_json, file4_json, 'test_json.txt', 'json'),
]


@pytest.mark.parametrize('file1, file2, result, format', cases)
def test_generate_diff(file1, file2, result, format):
    assert generate_diff(file1, file2, format) == read_file(result)
