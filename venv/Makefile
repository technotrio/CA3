install:
	pip install --upgrade pip&\
	pip install -r requirements.txt
lint:
	pylint --disable=C,R add.py
test:
	python -m pytest -vv --cov=add test_add.py