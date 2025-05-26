# Secure Data Encryption (Assignment 05)

A Python application for secure data encryption and handling using modern cryptographic techniques.

## 🔒 Features

- Secure data encryption and decryption
- Streamlit-based user interface
- Environment variable management for secure configuration
- Modern cryptographic implementations using the `cryptography` library

## 🛠️ Technologies Used

- Python
- Streamlit (UI Framework)
- Cryptography (for encryption/decryption)
- python-dotenv (for environment management)

## 📋 Prerequisites

- Python 3.x
- UV package manager

## 🚀 Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd 05-secure-data-encryption
```

2. Create and activate a virtual environment:
```bash
uv venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv add -r requirements.txt
```

## 🏃‍♂️ Running the Application

1. Make sure your virtual environment is activated
2. Run the Streamlit application:
```bash
streamlit run main.py
```

## 📦 Dependencies

- streamlit>=1.45.1
- cryptography
- python-dotenv

## 🔐 Security Notes

- Always keep your encryption keys secure
- Never commit sensitive data or .env files to version control
- Use strong encryption methods provided by the cryptography library

