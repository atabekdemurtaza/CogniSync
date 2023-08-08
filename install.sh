#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies using pip
pip install -r requirements.txt

# Run a project
python manage.py runserver

echo "Installation complete!"

