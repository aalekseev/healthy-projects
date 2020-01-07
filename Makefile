.PHONY: help black

help:
	@echo "Available comands:"
	@echo "    format - autoformat the source code with black"
	@echo "    test - run tests with py.test"
	@echo "    types - check the types with mypy"

format:
	black src example

test:
	py.test src

types:
	mypy src
