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

make lint:
	@poetry run flake8 brain_games

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml tests