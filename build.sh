#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

pipenv shell
python manage.py collectstatic --no-input
python manage.py migrate