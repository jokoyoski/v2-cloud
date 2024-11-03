#!/bin/sh
set -e 
# Apply migrations
python3 manage.py migrate

# Start the Django development server
python manage.py test cloud

python3 manage.py runserver 0.0.0.0:8000 & 
# Start the webpack server
npm run dev  
