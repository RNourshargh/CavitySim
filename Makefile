venv: setup.py
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -e .[test,docs,deploy]
	touch venv

test: venv
	./venv/bin/pytest --cov -rfsxEX --cov-report term-missing
