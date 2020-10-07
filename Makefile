install:
	poetry install
package-install:
	pip install --user dist/*.whl
build:
	poetry build
publish:
	poetry publish -r testpypi
lint:
	poetry run flake8 brain_games
brain-games:
	poetry run brain-games
even:
	poetry run brain-even