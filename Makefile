install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install dist/*.whl
help:
	poetry run gendiff -h
lint:
	poetry run flake8 gendiff
diff:
	poetry run gendiff ../file1.json ../file2.json
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml