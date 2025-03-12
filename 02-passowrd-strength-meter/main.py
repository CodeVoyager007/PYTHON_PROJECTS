import streamlit as st
import re
import random
import string
import pyperclip

# Custom CSS for dark mode styling with animations
st.markdown("""
    <style>
        body { 
            background-color: #181818; 
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton button { 
            background-color: #FF6347;
            color: white;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            padding: 8px 20px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton button:hover { 
            transform: translateY(-2px);
            background-color: #FF4500;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
        }
        .result-box {
            background-color: #222;
            padding: 15px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            border: 2px solid #FF6347;
            margin: 10px 0;
            animation: slideIn 0.5s ease-out;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .strength-bar {
            height: 12px;
            width: 100%;
            border-radius: 6px;
            margin: 15px 0;
            background: #ddd;
            overflow: hidden;
            position: relative;
        }
        .strength-bar::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: var(--strength);
            background: linear-gradient(90deg, #ff4444, #ff8c00, #00ff00);
            transition: width 1s ease-in-out;
        }
        @keyframes slideIn {
            from {
                transform: translateY(20px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        .suggestion-box {
            background-color: #2a2a2a;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            border-left: 4px solid #FF6347;
            animation: fadeIn 0.5s ease-out;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateX(-10px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        .stTextInput input {
            background-color: #2a2a2a;
            border: 2px solid #444;
            border-radius: 8px;
            color: white;
            padding: 12px;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #FF6347;
            box-shadow: 0 0 0 2px rgba(255, 99, 71, 0.2);
        }
        .sidebar .sidebar-content {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .score-display {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin: 15px 0;
            color: #FF6347;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check (with bonus points for longer passwords)
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Additional Security Checks
    if re.search(r"(.)\1{2,}", password):
        feedback.append("⚠️ Avoid repeating characters more than twice.")
    
    if re.search(r"123|abc|qwerty|password", password.lower()):
        feedback.append("⚠️ Avoid common patterns or sequences.")
    
    # Strength Rating
    if score >= 5:
        feedback.append("✅ Strong Password!")
    elif score >= 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return score, feedback

# Function to generate a strong password
def generate_strong_password():
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    # Ensure minimum requirements
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Add more random characters to reach minimum length of 12
    remaining_length = 8
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Add random characters while ensuring no more than 2 repeated characters
    while len(password) < 12:
        new_char = random.choice(all_chars)
        # Check if adding this character would create more than 2 repetitions
        if password.count(new_char) < 2:
            password.append(new_char)
    
    # Shuffle the password
    random.shuffle(password)
    
    # Ensure no common patterns
    password_str = ''.join(password)
    common_patterns = ['123', 'abc', 'qwerty', 'password', 'admin']
    
    # If password contains common patterns, regenerate
    while any(pattern in password_str.lower() for pattern in common_patterns):
        random.shuffle(password)
        password_str = ''.join(password)
    
    return password_str

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Add a sidebar with information
with st.sidebar:
    st.markdown("""
        <style>
            .sidebar-content {
                background-color: #1a1a1a;
                padding: 25px;
                border-radius: 15px;
                margin: 15px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .sidebar-header {
                color: #FF6347;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
                padding-bottom: 10px;
                border-bottom: 2px solid #FF6347;
            }
            .feature-list {
                list-style-type: none;
                padding: 0;
            }
            .feature-list li {
                margin: 12px 0;
                padding-left: 25px;
                position: relative;
                color: #e0e0e0;
            }
            .feature-list li:before {
                content: "✨";
                position: absolute;
                left: 0;
                color: #FF6347;
            }
            .requirements-list {
                list-style-type: none;
                padding: 0;
            }
            .requirements-list li {
                margin: 12px 0;
                padding-left: 25px;
                position: relative;
                color: #e0e0e0;
            }
            .requirements-list li:before {
                content: "✓";
                position: absolute;
                left: 0;
                color: #00ff00;
                font-weight: bold;
            }
            .section-divider {
                height: 2px;
                background: linear-gradient(to right, #FF6347, transparent);
                margin: 20px 0;
            }
            .footer {
                text-align: center;
                padding: 20px 0;
                margin-top: 30px;
                border-top: 1px solid #333;
                color: #888;
                font-size: 14px;
                animation: fadeIn 1s ease-in;
            }
            .footer span {
                color: #FF6347;
                font-weight: bold;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .heart {
                color: #FF6347;
                animation: heartbeat 1.5s ease-in-out infinite;
            }
            @keyframes heartbeat {
                0% { transform: scale(1); }
                50% { transform: scale(1.2); }
                100% { transform: scale(1); }
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # About Section
    st.markdown('<div class="sidebar-header">About</div>', unsafe_allow_html=True)
    st.markdown("""
        <ul class="feature-list">
            <li>Checking password complexity</li>
            <li>Providing real-time feedback</li>
            <li>Suggesting improvements</li>
            <li>Generating strong passwords</li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Password Requirements Section
    st.markdown('<div class="sidebar-header">Password Requirements</div>', unsafe_allow_html=True)
    st.markdown("""
        <ul class="requirements-list">
            <li>At least 8 characters</li>
            <li>Mix of uppercase and lowercase letters</li>
            <li>Numbers (0-9)</li>
            <li>Special characters (!@#$%^&*)</li>
            <li>No repeated characters</li>
            <li>No common patterns</li>
        </ul>
    """, unsafe_allow_html=True)
    
    # Footer with credits
    st.markdown("""
        <div class="footer">
            Coded with <span class="heart">❤️</span> By <span>Ayesha Mughal</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main content
password = st.text_input("Enter your password", type="password", placeholder="Type your password here...")

if password:
    with st.spinner("Analyzing password strength..."):
        try:
            score, feedback = check_password_strength(password)
            
            # Display feedback with animation
            for message in feedback:
                st.markdown(f'<div class="result-box">{message}</div>', unsafe_allow_html=True)
            
            # Visual Strength Bar with percentage
            strength_percentage = min(100, (score / 5) * 100)
            st.markdown(f'<div class="strength-bar" style="--strength: {strength_percentage}%"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="score-display">Strength Score: {score}/5 ({strength_percentage}%)</div>', unsafe_allow_html=True)
            
            # Suggestions for weak passwords
            if score < 5:
                st.subheader("🔑 Suggestions for a Stronger Password:")
                st.markdown('<div class="suggestion-box">', unsafe_allow_html=True)
                st.markdown("1. **Increase the length** of your password.")
                st.markdown("2. **Add a mix of uppercase and lowercase letters.**")
                st.markdown("3. **Include at least one number** (0-9).")
                st.markdown("4. **Add at least one special character** like !@#$%^&*.")
                st.markdown("5. **Avoid repeating characters** more than twice.")
                st.markdown("6. **Avoid common patterns** like '123' or 'abc'.")
                st.markdown('</div>', unsafe_allow_html=True)
                
                generated_password = generate_strong_password()
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f'<div class="result-box">💡 **Generated Secure Password:** `{generated_password}`</div>', unsafe_allow_html=True)
                    st.markdown("""
                    <div class="suggestion-box">
                        <strong>This password is guaranteed to have:</strong>
                        <ul>
                            <li>At least 12 characters</li>
                            <li>Uppercase and lowercase letters</li>
                            <li>Numbers and special characters</li>
                            <li>No more than 2 repeated characters</li>
                            <li>No common patterns</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("Copy", key="copy_button"):
                        pyperclip.copy(generated_password)
                        st.success("Copied to clipboard!")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.info("👆 Enter a password above to check its strength.")
