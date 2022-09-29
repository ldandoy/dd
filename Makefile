SOURCEDIR     = docs

init:
	pip install -r requirements.txt

test:
	py.test tests

doc:
	cd docs && sphinx-build -b html . html && cd ..

run:
	python src/__main__.py

exe:
	python -m auto_py_to_exe