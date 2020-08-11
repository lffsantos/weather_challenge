#!/bin/bash
.PHONY: default
.SILENT:

development:
	python manage.py runserver 0:8000

test:
	pytest