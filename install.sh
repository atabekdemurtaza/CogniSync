#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies using pip
pip install -r requirements.txt

# Run a project
python manage.py runserver --settings=config.settings.local

# Redis setup
echo "docker run -it --rm --name redis -p 6379:6379 redis"

# Test a request
echo "curl http://localhost:8000/api/products/ | json_pp"

echo "Installation complete!"

