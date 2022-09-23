SOURCEDIR     = docs

init:
	pip install -r requirements.txt

test:
	py.test tests

doc:
	sphinx-build -b html docs docs/build

run:
	python src/__main__.py

exe:
	python -m auto_py_to_exe