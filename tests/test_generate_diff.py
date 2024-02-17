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

flat_cases = [
    (flat_json, flat_output),
    (flat_yml, flat_output),
    (flat_json_yaml, flat_output),
]


@pytest.mark.parametrize('path, result', flat_cases)
def test_generate_diff(path, result):
    assert generate_diff(path) == result
