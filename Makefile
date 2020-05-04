DC = $(shell which docker-compose)

artifacts = docs/site

.PHONY: clean

default: help
	@echo ""
	@echo "You need to specify a subcommand."
	@exit 1

help:
	@echo "build		- buld the docker images"
	@echo "run			- start the build in Django development server"
	@echo "init			- initialize the database"
	@echo "runshell  	- run and enter to a bash shell with the ports bounded"
	@echo "dbshell		- enter to the database shell"
	@echo "test			- run the test suit"
	@echo "docs-watch	- start the development server for the documentation on the port 8080"
	@echo "docs-build   - build the documentation"

build:
	${DC} build

run:
	${DC} up -d

runshell:
	${DC} run --service-ports web bash

dbshell:
	${DC} run web poetry run python manage.py dbshell

lint:
	${DC} run web poetry run black . --check --exclude venv --exclude migrations

format:
	${DC} run web poetry run black . --exclude venv --exclude migrations

test:
	${DC} run web poetry run pytest --reuse-db

frontend:
	${DC} run node yarn install

frontend-build:
	${DC} run node yarn run parcel build assets/js/app.js assets/css/style.css

frontend-watch:
	${DC} run node yarn run parcel watch assets/js/app.js assets/css/style.css

init: frontend-build
	${DC} run web bin/wait-for-it.sh postgres:5432
	${DC} run web bin/bootstrap.sh

docs-watch:
	${DC} run -p 8080:8080 web poetry run mkdocs serve -a 0.0.0.0:8080 -f docs/mkdocs.yml

docs-build:
	${DC} run web poetry run mkdocs build -f docs/mkdocs.yml

clean: 
	rm -rf ${artifacts}

