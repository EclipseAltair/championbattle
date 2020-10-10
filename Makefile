clean-pyc:
	find . -name "*.pyc" -delete

run-site: clean-pyc
	DJANGO_SETTINGS_MODULE=championbattle.settings.dev ./manage.py runserver 8000
