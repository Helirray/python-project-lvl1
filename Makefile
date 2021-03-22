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
	@poetry run pytest --cov=brain_games --cov-report xml tests

test:
	@poetry run pytest brain_games tests

selfcheck:
	@poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build