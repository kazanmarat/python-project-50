build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff

install:
	poetry install

check:
	poetry run flake8 gendiff
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml


# test-coverage:
# 	poetry run pytest --cov

# test:
# 	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json 
