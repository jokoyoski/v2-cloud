#!/bin/sh
# Apply migrations

cd app
python3 manage.py migrate

# Run both Django and Webpack
# Run Django server in the background
python3 manage.py runserver 0.0.0.0:8000 & 

# Start Webpack in the foreground
npm run dev
