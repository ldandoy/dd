SOURCEDIR     = docs

init:
	pip install -r requirements.txt
	sphinx-quickstart

test:
	py.test tests

doc:
	sphinx-build -b html docs docs/build

run:
	python src/main.py

exe:
	python -m auto_py_to_exe