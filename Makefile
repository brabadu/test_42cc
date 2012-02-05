MANAGE=django-admin.py

test:
	python manage.py test
	# PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) test main

run:
	python manage.py runserver
	# PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) runserver

syncdb:
	python manage.py syncdb
	# PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) syncdb --noinput
