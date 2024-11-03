

# Project Setup Guide

## Steps to Initialize

1. Navigate to the project directory containing the Docker Compose configuration:

2. Build and launch the Docker containers:
   ```bash
   docker-compose build && docker-compose up
   ```

   This command initializes both the Django server and the Webpack server.

3. Open the application in your browser:
   [http://localhost:8000/](http://localhost:8000/)

## Key Features

- **Automated Testing**: The `entrypoint.sh` script now includes a test command, ensuring that tests run automatically during the Docker build and startup process. If any tests fail, the build will halt.

- **Database Configuration Update**: The SQLite database path has been moved to a configuration setting. This helps segregate configuration files, especially for sensitive data, and maintains better project organization. The path is now stored in the `.env` file as `DB_PATH=db.sqlite3`.
Make sure you create a .env file inside the /app directory
DB_PATH=db.sqlite3

- **Service Layer Introduction**: A service layer has been introduced to act as an intermediary between views and models. This abstraction improves the separation of concerns within the application.

- **CSS Loading Configuration**: Webpack is now configured to handle CSS files. This enhancement ensures the proper loading of styled components, contributing to a polished UI experience.p