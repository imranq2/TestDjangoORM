.PHONY: init
init:
	python manage.py makemigrations polls
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver
