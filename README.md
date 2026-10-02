# Authentication System

A beginner-friendly Python authentication system that demonstrates
user registration, login, password hashing, validation, and logout.

## Features

- User registration
- Username validation
- Duplicate username prevention
- Password validation
- Password hashing
- Secure password input using `getpass`
- User login
- Logout
- JSON-based local data storage
- Case-insensitive usernames

## Technologies

- Python
- JSON
- hashlib
- getpass

## How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL

Navigate into the project:
cd Authentication-System

Run the application:
python3 auth_system.py


## Security Note

This project uses SHA-256 hashing to demonstrate the basic concept
of password hashing.

For production applications, passwords should be stored using
password-specific algorithms such as Argon2id, bcrypt, or scrypt
with appropriate salts and security settings.

Project Purpose

This project was created as part of a Software Engineering learning
roadmap to practice Python functions, JSON storage, authentication,
validation, hashing, and Git/GitHub workflows.