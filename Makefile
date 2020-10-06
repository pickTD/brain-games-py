install:
	poetry install
build:
	poetry build
publish:
	poetry publish -r testpypi
package-install:
	pip install --upgrade --force-reinstall --user dist/*.whl
brain-games:
	poetry run brain-games