import pytest
import os
from gendiff import generate_diff


path_fixtures = os.path.join('tests', 'fixtures')

with open(os.path.join(path_fixtures, 'test_flat.txt')) as flat_file:
    flat_output = flat_file.read()
with open(os.path.join(path_fixtures, 'test_rec.txt')) as rec_file:
    rec_output = rec_file.read()
with open(os.path.join(path_fixtures, 'test_plain.txt')) as rec_plain:
    rec_output_plain = rec_plain.read()

file1_json = os.path.join(path_fixtures, 'filepath1.json')
file2_json = os.path.join(path_fixtures, 'filepath2.json')
file1_yml = os.path.join(path_fixtures, 'filepath1.yml')
file2_yml = os.path.join(path_fixtures, 'filepath2.yml')
file3_json = os.path.join(path_fixtures, 'filepath3.json')
file4_json = os.path.join(path_fixtures, 'filepath4.json')
file3_yml = os.path.join(path_fixtures, 'filepath3.yml')
file4_yml = os.path.join(path_fixtures, 'filepath4.yml')


cases = [
    (file1_json, file2_json, flat_output, 'stylish'),
    (file1_yml, file2_yml, flat_output, 'stylish'),
    (file1_json, file2_yml, flat_output, 'stylish'),
    (file3_json, file4_json, rec_output, 'stylish'),
    (file3_yml, file4_yml, rec_output, 'stylish'),
    (file3_json, file4_json, rec_output_plain, 'plain'),
]


@pytest.mark.parametrize('file1, file2, result, format', cases)
def test_generate_diff(file1, file2, result, format):
    assert generate_diff(file1, file2, format) == result
