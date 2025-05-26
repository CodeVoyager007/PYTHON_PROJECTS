# 🛡️ Secure Data Encryption System

A Streamlit-based secure data storage and retrieval system that allows users to encrypt and decrypt data using unique passkeys.

## Features

### Security
- PBKDF2 password hashing with unique salts
- Fernet symmetric encryption for data
- Time-based lockout after failed attempts
- Secure password verification using constant-time comparison
- In-memory session management
- JSON-based persistent storage

### User Management
- User registration with password confirmation
- Secure login system
- Per-user data isolation
- Failed attempt tracking
- Automatic session timeout

### Data Management
- Secure data encryption with unique passkeys
- Data retrieval with passkey verification
- Data deletion with passkey verification
- Chronological data organization
- User-specific data views

## Setup

1. Make sure you have Python 3.8 or higher installed
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage

### 1. Account Management
- **Register**: Create a new account with username and password
- **Login**: Access your encrypted data securely
- **Logout**: End your session safely

### 2. Data Operations
- **Store Data**: 
  - Enter your text
  - Create a unique passkey
  - Save the encrypted text safely
- **Retrieve Data**:
  - Enter the encrypted text
  - Provide the correct passkey
  - View your decrypted data
- **Manage Data**:
  - View all your stored entries
  - Delete entries with passkey verification
  - Chronological organization

### 3. Security Features
- Three failed attempts trigger a 5-minute lockout
- Each user's data is isolated and protected
- Passwords are securely hashed with PBKDF2
- All data is encrypted using Fernet symmetric encryption

## Technical Details

- **Frontend**: Streamlit
- **Encryption**: cryptography.fernet
- **Password Hashing**: PBKDF2 with SHA-256
- **Storage**: JSON-based file system
- **Session Management**: Streamlit session state
- **Error Handling**: Comprehensive validation and error messages

## Security Best Practices

- Never share your passkeys
- Use strong, unique passwords
- Log out after each session
- Keep your encrypted text backups secure
- Don't store sensitive information in plain text
