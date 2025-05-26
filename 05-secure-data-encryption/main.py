import streamlit as st
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import time
import json
import os
import secrets

# File paths and settings
DATA_FILE = "encrypted_data.json"
USERS_FILE = "users.json"
SALT_LENGTH = 16
MAX_ATTEMPTS = 3 
LOCKOUT_TIME = 300 
PBKDF2_ITERATIONS = 480000

# Helper function to load data from JSON file
def load_saved_data():
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Helper function to load users from JSON file
def load_saved_users():
    
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save encrypted data to file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(st.session_state.stored_data, file)

# Save user information to file
def save_users():
    with open(USERS_FILE, 'w') as file:
        json.dump(st.session_state.users, file)

# Initialize the app's session state (runs once at startup)
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    # Generate encryption key and setup cipher
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.key)
    # Load saved data
    st.session_state.stored_data = load_saved_data()
    st.session_state.users = load_saved_users()
    st.session_state.failed_attempts = {}
    st.session_state.is_authenticated = False
    st.session_state.current_user = None
    st.session_state.current_page = "login"

# Create a random salt for password hashing
def generate_salt():
    random_bytes = secrets.token_bytes(SALT_LENGTH)
    return base64.b64encode(random_bytes).decode('utf-8')

# Hash a password with optional salt
def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    # Generate new salt if none provided
    salt = generate_salt() if salt is None else salt
    
    # Convert salt from string to bytes
    salt_bytes = base64.b64decode(salt.encode('utf-8'))
    
    # Create the password hasher
    password_hasher = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_bytes,
        iterations=PBKDF2_ITERATIONS,
    )
    
    # Hash the password
    hashed_password = password_hasher.derive(password.encode())
    hashed_password_str = base64.b64encode(hashed_password).decode('utf-8')
    
    return hashed_password_str, salt

# Check if a password matches its hash
def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    # Hash the provided password with the same salt
    calculated_hash, _ = hash_password(password, salt)
    # Compare the hashes securely
    return secrets.compare_digest(calculated_hash, stored_hash)

# Encrypt text data
def encrypt_data(text: str) -> str:
    """Encrypt the input text using Fernet encryption."""
    # Convert text to bytes, encrypt it, and convert back to string
    text_bytes = text.encode()
    encrypted_bytes = st.session_state.cipher.encrypt(text_bytes)
    return encrypted_bytes.decode()
# Decrypt text data
def decrypt_data(encrypted_text: str, passkey: str) -> str:
    """Decrypt the encrypted text if passkey is correct."""
    user = st.session_state.current_user
    attempts = get_user_attempts(user)
    
    # Check if account is locked
    if attempts["last_attempt"]:
        time_passed = time.time() - attempts["last_attempt"]
        if time_passed < LOCKOUT_TIME:
            remaining_time = int(LOCKOUT_TIME - time_passed)
            st.error(f"🔒 Account locked. Wait {remaining_time} seconds.")
            return None

    # Reset attempts if lockout time has passed
    if attempts["count"] >= MAX_ATTEMPTS:
        if time.time() - attempts["last_attempt"] >= LOCKOUT_TIME:
            attempts["count"] = 0
            attempts["last_attempt"] = None
        else:
            remaining_time = int(LOCKOUT_TIME - (time.time() - attempts["last_attempt"]))
            st.error(f"🔒 Account locked. Wait {remaining_time} seconds.")
            return None

    # Check if passkey is correct
    passkey_hash, _ = hash_password(passkey, st.session_state.users[user]["salt"])
    
    # Look for matching data
    for data in st.session_state.stored_data.values():
        if (data["encrypted_text"] == encrypted_text and 
            data["passkey"] == passkey_hash and 
            data["user"] == user):
            # Reset failed attempts on success
            attempts["count"] = 0
            attempts["last_attempt"] = None
            # Decrypt and return the data
            decrypted_bytes = st.session_state.cipher.decrypt(encrypted_text.encode())
            return decrypted_bytes.decode()
    
    # Increment failed attempts
    attempts["count"] += 1
    if attempts["count"] >= MAX_ATTEMPTS:
        attempts["last_attempt"] = time.time()
        st.session_state.is_authenticated = False
    
    return None

# Track failed login attempts
def get_user_attempts(username: str) -> dict:
    # Create new attempt tracking if user not found
    if username not in st.session_state.failed_attempts:
        st.session_state.failed_attempts[username] = {
            "count": 0,
            "last_attempt": None
        }
    return st.session_state.failed_attempts[username]

# Get all data for current user
def get_user_data():
    user = st.session_state.current_user
    user_data = []
    
    # Collect all entries for current user
    for encrypted_text, data in st.session_state.stored_data.items():
        if data["user"] == user:
            user_data.append({
                "encrypted_text": encrypted_text,
                "created_at": data.get("created_at", time.time())
            })
    
    # Sort by creation time (newest first)
    return sorted(user_data, key=lambda x: x["created_at"], reverse=True)
# UI 
st.title("🔒 Secure Data Encryption System")

# Login page
def show_login_page():
    st.subheader("👤 Login")
    # Create login form
    with st.form("login_form"):
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        submit = st.form_submit_button("Login")
        
        if submit and username and password:
            # Check if user exists
            if username in st.session_state.users:
                user_info = st.session_state.users[username]
                # Verify password
                if verify_password(password, user_info["password"], user_info["salt"]):
                    st.session_state.current_user = username
                    st.session_state.is_authenticated = True
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Wrong password!")
            else:
                st.error("❌ User not found!")
    
    st.markdown("---")
    if st.button("Create New Account"):
        st.session_state.current_page = "register"
        st.rerun()
# Registration page
def show_register_page():
    st.subheader("📝 Register")
    # Create registration form
    with st.form("register_form"):
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")
        submit = st.form_submit_button("Register")
        
        if submit:
            if not username or not password or not confirm_password:
                st.error("⚠️ All fields are required!")
            elif username in st.session_state.users:
                st.error("❌ Username already exists!")
            elif password != confirm_password:
                st.error("❌ Passwords don't match!")
            else:
                # Create new user
                password_hash, salt = hash_password(password)
                st.session_state.users[username] = {
                    "password": password_hash,
                    "salt": salt,
                    "created_at": time.time()
                }
                save_users()
                st.success("✅ Registration successful! Please login.")
                st.session_state.current_page = "login"
                st.rerun()
    
    st.markdown("---")
    if st.button("Back to Login"):
        st.session_state.current_page = "login"
        st.rerun()

# Main Navigation
if not st.session_state.is_authenticated:
    # Show register or login page
    if st.session_state.current_page == "register":
        show_register_page()
    else:
        show_login_page()
else:
    # Main menu for logged-in users
    menu = ["Home", "Store Data", "Retrieve Data", "Manage Data", "Logout"]
    choice = st.sidebar.selectbox("Navigation", menu)

    # Show user info
    st.sidebar.success(f"👤 Logged in as: {st.session_state.current_user}")
    
    # Show failed attempts warning
    user = st.session_state.current_user
    attempts = get_user_attempts(user)
    if attempts["count"] > 0:
        st.sidebar.warning(f"⚠️ Failed attempts: {attempts['count']}/{MAX_ATTEMPTS}")

    # Handle menu choices
    if choice == "Logout":
        st.session_state.current_user = None
        st.session_state.is_authenticated = False
        st.session_state.current_page = "login"
        st.success("👋 Logged out successfully!")
        st.rerun()
        
    elif choice == "Home":
        st.subheader("🏠 Welcome!")
        st.write("This app lets you securely store and retrieve data using passwords.")
        st.info("📌 Your data is encrypted and stored safely.")
        
        # Count user's stored entries
        entry_count = 0
        for item in st.session_state.stored_data.values():
            if item["user"] == st.session_state.current_user:
                entry_count += 1
        st.metric("Your Stored Entries", entry_count)

    elif choice == "Store Data":
        st.subheader("📂 Store Data")
        
        # Create data storage form
        with st.form("store_data_form"):
            user_data = st.text_area("Your Data:")
            passkey = st.text_input("Password:", type="password")
            submit_button = st.form_submit_button("Save & Encrypt")

            if submit_button:
                if not user_data or not passkey:
                    st.error("⚠️ Please fill all fields!")
                else:
                    # Encrypt and store the data
                    passkey_hash, _ = hash_password(passkey, st.session_state.users[user]["salt"])
                    encrypted_text = encrypt_data(user_data)
                    st.session_state.stored_data[encrypted_text] = {
                        "encrypted_text": encrypted_text,
                        "passkey": passkey_hash,
                        "user": st.session_state.current_user,
                        "created_at": time.time()
                    }
                    save_data()
                    st.success("✅ Data saved!")
                    st.code(encrypted_text, language="text")
                    st.info("📝 Save this encrypted text to access your data later!")

    elif choice == "Retrieve Data":
        st.subheader("🔍 Retrieve Data")
        
        # Check authentication
        if not st.session_state.is_authenticated:
            st.warning("🔒 Please login first!")
            st.rerun()
        
        # Create data retrieval form
        with st.form("retrieve_data_form"):
            encrypted_text = st.text_area("Encrypted Data:")
            passkey = st.text_input("Password:", type="password")
            submit_button = st.form_submit_button("Decrypt")

            if submit_button:
                if not encrypted_text or not passkey:
                    st.error("⚠️ Please fill all fields!")
                else:
                    # Try to decrypt the data
                    decrypted_text = decrypt_data(encrypted_text, passkey)
                    if decrypted_text:
                        st.success("✅ Data decrypted!")
                        st.code(decrypted_text, language="text")
                    else:
                        user = st.session_state.current_user
                        attempts = get_user_attempts(user)
                        remaining = MAX_ATTEMPTS - attempts["count"]
                        if remaining > 0:
                            st.error(f"❌ Wrong password! {remaining} attempts left.")
                        else:
                            st.error("❌ Too many attempts! Account locked.")

    elif choice == "Manage Data":
        st.subheader("📋 Your Stored Data")
        user_data = get_user_data()
        
        if not user_data:
            st.info("No data stored yet.")
        else:
            st.write("Your entries:")
            
            # Show each entry
            for idx, data in enumerate(user_data):
                with st.expander(f"Entry {idx + 1}"):
                    st.code(data["encrypted_text"], language="text")
                    col1, col2 = st.columns([3, 1])
                    
                    # Delete entry 
                    with col1:
                        delete_key = st.text_input("Password to delete:", 
                                                 type="password", 
                                                 key=f"delete_key_{idx}")
                    with col2:
                        if st.button("Delete", key=f"delete_{idx}", type="primary"):
                            if not delete_key:
                                st.error("⚠️ Enter password!")
                            else:
                                # Verify password and delete
                                passkey_hash, _ = hash_password(delete_key, 
                                                             st.session_state.users[user]["salt"])
                                stored_data = st.session_state.stored_data.get(data["encrypted_text"])
                                
                                if stored_data and stored_data["passkey"] == passkey_hash:
                                    del st.session_state.stored_data[data["encrypted_text"]]
                                    save_data()
                                    st.success("✅ Entry deleted!")
                                    st.rerun()
                                else:
                                    st.error("❌ Wrong password!")
