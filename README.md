# password-programm

## Author
Anfalova Yana

## Description
Simple console application for storing and generating passwords.

## Features
1)Add passwords
2)Generate passwords
3)Delete passwords
4)Save/load JSON

## Architecture
The project follows MVC pattern:

- Model: PasswordRecord
- Controller: PasswordController
- Services:
  - StorageService (JSON storage)
  - PasswordService (password generation)
  - ValidationService (input validation)


## Example
1. Add password:
Service: Gmail
Username: user123
Password: qwerty

2. Generate password:
Length: 8

Output:
Password: A8fK2LmP

## How to run
python main.py

## How to run tests
python -m unittest tests/test_passwords.py
