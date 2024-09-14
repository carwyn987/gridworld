# Makefile for packaging

# Rule to build the package
build:
	python3 -m build

# Rule to upload the package to TestPyPI
upload:
	python3 -m twine upload --repository testpypi dist/*

# Rule to run the tests
test:
	python3 -m unittest discover -s tests

# Rule to clean up the build and dist directories
clean:
	rm -rf build dist

# Rule to run all targets (build, test, upload)
all: build test upload

# Specify the default target (all)
.DEFAULT_GOAL := all