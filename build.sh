#!/usr/bin/env bash

set -o errexit  # exit on error

pipenv install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate