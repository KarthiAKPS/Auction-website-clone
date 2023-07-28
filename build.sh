#!/bin/bash

echo "Building the project..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput