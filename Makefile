.PHONY: setup test build check serve
setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	bundle install
test:
	.venv/bin/python -m unittest discover -s tests
	.venv/bin/python scripts/publish.py validate
build:
	bundle exec jekyll build --strict_front_matter
check: test build
	.venv/bin/python scripts/check_site.py
serve:
	bundle exec jekyll serve --host 127.0.0.1 --port 4173
