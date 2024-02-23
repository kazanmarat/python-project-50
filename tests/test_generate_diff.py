import pytest
import os
from gendiff import generate_diff


path_fixtures = os.path.join('tests', 'fixtures')

with open(os.path.join(path_fixtures, 'test_flat.txt')) as flat_file:
    flat_output = flat_file.read()
flat_json = (os.path.join(path_fixtures, 'filepath1.json'),
             os.path.join(path_fixtures, 'filepath2.json'))
flat_yml = (os.path.join(path_fixtures, 'filepath1.yml'),
            os.path.join(path_fixtures, 'filepath2.yml'))
flat_json_yaml = (os.path.join(path_fixtures, 'filepath1.json'),
                  os.path.join(path_fixtures, 'filepath2.yml'))

with open(os.path.join(path_fixtures, 'test_rec.txt')) as rec_file:
    rec_output = rec_file.read()
rec_json = (os.path.join(path_fixtures, 'filepath3.json'),
            os.path.join(path_fixtures, 'filepath4.json'))
rec_yaml = (os.path.join(path_fixtures, 'filepath3.yml'),
            os.path.join(path_fixtures, 'filepath4.yml'))

cases = [
    (flat_json, flat_output),
    (flat_yml, flat_output),
    (flat_json_yaml, flat_output),
    (rec_json, rec_output),
    (rec_yaml, rec_output),
]


@pytest.mark.parametrize('path, result', cases)
def test_generate_diff(path, result):
    assert generate_diff(path) == result
