install:
	poetry install
build: check
	poetry build
package-install:
	python3 -m pip install dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
selfcheck:
	poetry check
check: selfcheck test lint
setup: install build package-install