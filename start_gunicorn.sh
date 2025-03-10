#!/bin/bash
source /var/www/charity/CharityWebsite/.venv/bin/activate  # Activate your virtual environment
exec gunicorn --bind unix:/var/www/charity/CharityWebsite/gunicorn.sock --workers 3 --threads 2 --timeout 30 Charity.wsgi:application
