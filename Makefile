setup: install build package-install
install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
help:
	poetry run gendiff -h
lint:
	poetry run flake8 gendiff
diff:
	poetry run gendiff ../file1.json ../file2.json
test:
	poetry run pytest
test-cov:
	poetry run pytest --cov=gendiff