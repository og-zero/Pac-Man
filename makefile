PYTHON := python3
SRC := src

install:
	uv sync

run:
	uv run $(PYTHON) -m $(SRC)

debug:
	uv run $(PYTHON) -m pdb -m $(SRC)

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache

lint:
	-uv run flake8 .
	-uv run mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

.PHONY:	install run debug clean lint lint-strict