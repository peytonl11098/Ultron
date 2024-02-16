---
toc: true
comments: false
layout: post
title: Jinja 2 Lesson
author: Nitin, Sergi, Ishan, Saathvik, Akshay
description: Week 20 Plans
courses: { csp: {week: 20} }
type: tangibles
---

## Jinja 2 Overview
- Jinja2 is a templating engine for Python.
- Widely used in web development frameworks like Flask and Django.
- Supports template inheritance for creating modular and reusable code.
- Provides flexible syntax for embedding Python-like expressions in templates.
- Offers built-in filters for data manipulation and formatting.
- Supports control structures like loops and conditionals.
- Automatically escapes HTML characters by default, enhancing web application security.

## Creating and Migrating database
The first object is to create and migrate a database. Run the script below to ensure database is created, primed, and has some starting data. Anytime a developer changes schema, this script needs to be run.

```bash
# Setup database and init data
# open terminal to root directory of project
./migrate.sh
```  

```bash
# Set environment variables
export FLASK_APP=main
export PYTHONPATH=.:$PYTHONPATH
```

- These lines set environment variables. FLASK_APP is set to main, indicating the main Flask application to be run. PYTHONPATH is updated to include the current directory, allowing Python to find modules and packages in the current directory.

```bash
# Check if sqlite3 is installed
if ! command -v sqlite3 &> /dev/null; then
    echo "Error: sqlite3 is not installed. Please install it before running this script."
    exit 1
fi
```
- This block checks if the sqlite3 command is available. If not, it displays an error message and exits with a status code of 1.

```bash
# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed. Please install it before running this script."
    exit 1
fi
```
- Similar to the previous block, this one checks for the presence of python3 command and exits with an error message if it's not found.

```bash
# Check if Flask is installed
if ! python3 -m flask --version &> /dev/null; then
    echo "Error: Flask is not installed. Please install it before running this script."
    exit 1
fi
```
- This block checks if Flask is installed by attempting to run python3 -m flask --version. If Flask is not found, it exits with an error message.

```bash
# Check if the migration directory exists
if [ ! -d "migrations" ]; then
    echo "Initializing migration for the first time..."
    python3 -m flask db init
fi
```
 - This section checks if the directory migrations exists. If not, it initializes Flask database migrations using python3 -m flask db init.

```bash
# . restore from backup before migration
if [ ! -e "instance/volumes/sqlite.db" ] && [ -e "instance/volumes/sqlite-backup.db" ]; then
    echo "No sqlite.db found, using sqlite-backup.db to generate the file."
    
    # Copy backup file to primary (sqlite.db)
    cp "instance/volumes/sqlite-backup.db" "instance/volumes/sqlite.db"

    # Extract the new Alembic version from the backup database
    backup_version=$(sqlite3 instance/volumes/sqlite.db "SELECT version_num FROM alembic_version;")
    echo "Version ${backup_version} detected"

    python3 -m flask db stamp "${backup_version}"

# Check if sqlite.db exists
# . backup before migration
elif [ -e "instance/volumes/sqlite.db" ]; then
    # Create a timestamp for the backup file
    timestamp=$(date "+%Y%m%d%H%M%S")
    backup_file="instance/volumes/sqlite-backup-${timestamp}.db"

    # Backup SQLite database
    sqlite3 instance/volumes/sqlite.db ".backup instance/volumes/sqlite-backup.db"
    sqlite3 instance/volumes/sqlite.db ".backup ${backup_file}"
fi

# Perform database migrations
python3 -m flask db migrate

# Perform database upgrade
python3 -m flask db upgrade

# Run a custom command to generate data
python3 -m flask custom generate_data
```
## In-depth look of this piece
```bash
if [ ! -e "instance/volumes/sqlite.db" ] && [ -e "instance/volumes/sqlite-backup.db" ]; then
```
- This line checks if sqlite.db does not exist (! -e "instance/volumes/sqlite.db") AND sqlite-backup.db exists (-e "instance/volumes/sqlite-backup.db"). If both conditions are true, the code block inside the if statement will be executed.

```bash
echo "No sqlite.db found, using sqlite-backup.db to generate the file."
```
- This line simply prints a message indicating that sqlite.db is not found and sqlite-backup.db will be used to generate the file.

```bash
cp "instance/volumes/sqlite-backup.db" "instance/volumes/sqlite.db"
```
- This line copies the contents of sqlite-backup.db to sqlite.db, essentially restoring the database from the backup file.

```bash
backup_version=$(sqlite3 instance/volumes/sqlite.db "SELECT version_num FROM alembic_version;")
echo "Version ${backup_version} detected"
```
- Here, it retrieves the version number (version_num) from the alembic_version table of the newly restored database (sqlite.db) using the sqlite3 command-line tool. It then prints out the detected version number.

```bash
python3 -m flask db stamp "${backup_version}"
```
- This line runs a Flask database migration command (python3 -m flask db stamp) and passes the detected version number ("${backup_version}") as an argument. This essentially stamps the database with the detected version number, indicating that it is up to date with the migrations corresponding to that version.

```bash
elif [ -e "instance/volumes/sqlite.db" ]; then
```
- The elif part of the script handles the situation where sqlite.db already exists:
- This line checks if sqlite.db exists. If it does, the code block inside the elif statement will be executed.

```bash
timestamp=$(date "+%Y%m%d%H%M%S")
backup_file="instance/volumes/sqlite-backup-${timestamp}.db"
```
- These lines generate a timestamp and create a unique backup file name based on the timestamp.

```bash
sqlite3 instance/volumes/sqlite.db ".backup instance/volumes/sqlite-backup.db"
sqlite3 instance/volumes/sqlite.db ".backup ${backup_file}"
```
- This pair of commands backs up the existing sqlite.db database. It first creates a general backup named sqlite-backup.db and then creates a timestamped backup file (sqlite-backup-${timestamp}.db).

```bash
python3 -m flask db migrate
```
- Initiates database migrations using Flask's migration system.
- These migration scripts capture changes such as adding or modifying tables, columns, or indexes in the database schema.

```bash
python3 -m flask db upgrade
```
- Applies database migrations to the database.
- After running this command, the database structure reflects the changes specified in the migration scripts.

```bash
python3 -m flask custom generate_data
```
- Executes a custom Flask command to generate data.
- The custom command generate_data may perform tasks such as populating the database with initial data, creating sample records for testing purposes, or performing any other data generation tasks required by the application.

# Summary and Purpose
- Database Environment Setup: It ensures that the necessary environment variables are set to facilitate the Flask application's operation.
- Dependency Checks: It checks if essential dependencies (sqlite3, python3, and Flask) are installed on the system. This helps ensure that the script can run successfully.
- Flask Migration Initialization: If the migrations directory doesn't exist, it initializes Flask database migrations. This is a crucial step in managing database schema changes over time.
- Database Backup and Restore: It handles scenarios where the main database (sqlite.db) may need to be restored from a backup (sqlite-backup.db) before migration. This ensures data integrity during the migration process.
- Database Migration: It performs database migrations using Flask's migration commands. This step is essential for applying schema changes and updates to the database structure.
- Data Generation: Finally, it executes a custom command (generate_data) to generate additional data, which can be useful for testing or initializing the application with some starting data.
