init: .env
	PIPENV_VENV_IN_PROJECT="enabled" pipenv install --dev

.env:
	cp .env.example .env

PHONY=run_tests
run_tests: init
	PYTHONPATH=PYTHONPATH:./common/lib pipenv run pytest