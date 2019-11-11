default:
	# Install dependent libraries
	pip install -r requirements.txt
	# Migrate Database
	python manage.py migrate

run:default
	# Start plot emitter
	python manage.py runserver

