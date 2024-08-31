---

# 0x00-personal_data

This project focuses on handling and protecting Personally Identifiable Information (PII) in Python. It includes tasks to obfuscate sensitive data in logs, encrypt passwords, and authenticate database connections securely using environment variables.

## Learning Objectives

- Understand what constitutes Personally Identifiable Information (PII).
- Implement a log filter to obfuscate PII fields.
- Encrypt passwords and validate their authenticity.
- Securely connect to a database using environment variables.

## Requirements

- **Python Version:** Python 3.7
- **Operating System:** Ubuntu 18.04 LTS
- **Code Style:** Pycodestyle (version 2.5)

### General Requirements

- All files must be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- All code should conform to the `pycodestyle` style guide.
- Files must be executable.
- The length of files will be tested using `wc`.
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions (inside and outside a class) should have documentation.
- Functions should be type annotated.

## Tasks

### 0. Regex-ing

Implement a `filter_datum` function that returns a log message with specified fields obfuscated. Use regex to replace occurrences of certain field values.

### 1. Log Formatter

Update the `RedactingFormatter` class to filter sensitive fields in log records. Implement the `format` method to apply the `filter_datum` function on log messages.

### 2. Create Logger

Implement a `get_logger` function that configures a logger named `user_data`. The logger should use `RedactingFormatter` and handle up to `INFO` level logs. Define a `PII_FIELDS` tuple containing fields considered sensitive.

### 3. Connect to Secure Database

Implement a `get_db` function to securely connect to a MySQL database using credentials from environment variables. Use the `mysql-connector-python` package for the connection.

### 4. Read and Filter Data

Implement a `main` function to retrieve all rows in the `users` table from the database and log each row with sensitive fields filtered out.

### 5. Encrypting Passwords

Implement a `hash_password` function that returns a salted, hashed password using the `bcrypt` package.

### 6. Check Valid Password

Implement an `is_valid` function that checks if a provided password matches the hashed password using `bcrypt`.

## Setup

1. **Install Dependencies:**
   ```bash
   pip3 install mysql-connector-python bcrypt
   ```

2. **Set Environment Variables:**
   ```bash
   export PERSONAL_DATA_DB_USERNAME='root'
   export PERSONAL_DATA_DB_PASSWORD='your_password'
   export PERSONAL_DATA_DB_HOST='localhost'
   export PERSONAL_DATA_DB_NAME='your_db_name'
   ```

3. **Run Tests:**
   Ensure all tasks work correctly by running the provided main files.

## Author

- **Innocent Manda** - [GitHub: chipatenii](https://github.com/chipatenii)  
- Email: innocentmanda70@gmail.com

---
