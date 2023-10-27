#!/usr/bin/env bash
# exit on error
set -o errexit

python3.9 -m pip install -r requirements.txt

echo "colecting Static..."
python3.9 manage.py collectstatic --no-input

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate