install:
	poetry install
build:
	poetry build
publish:
	poetry publish -r testpypi
package-install:
	pip install --upgrade --force-reinstall --user dist/*.whl
lint:
	poetry run flake8 brain_games
brain-games:
	poetry run brain-games