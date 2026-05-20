install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

lint:
# pylint --disable=R,C hello.py
	pylint --disable=R,C main.py

test:
# python -m pytest -vv --cov=hello test_hello.py
	python -m pytest -vv --cov=main test_main.py
