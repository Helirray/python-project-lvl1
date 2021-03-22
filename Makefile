install:
	@poetry install

brain-games:
	@poetry run brain-games

build:
	@poetry build

publish:
	@poetry publish --dry-run

package-install:
	@python3 -m pip install --user dist/*.whl

lint:
	@poetry run flake8 brain_games

test-coverage:
	@poetry run pytest --cov=hexlet_python_package --cov-report xml tests

test:
	@poetry run pytest hexlet_python_package tests

selfcheck:
	@poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build