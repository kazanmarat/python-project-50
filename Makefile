build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

test:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json 
