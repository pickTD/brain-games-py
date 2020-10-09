install:
	poetry install
package-install:
	pip install --no-cache-dir --user dist/*.whl
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
calc:
	poetry run brain-calc
gcd:
	poetry run brain-gcd
prog:
	poetry run brain-progression
prime:
	poetry run brain-prime