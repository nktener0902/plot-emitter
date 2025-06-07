# Setup
.PHONY: default
default:
	# Install dependent libraries
	pip install -r requirements.txt
	# Migrate Database
	python manage.py migrate

# Setup and run the server
.PHONY: run
run:default
	python manage.py runserver
