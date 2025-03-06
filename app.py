# import re
# import random
# import math
# import streamlit as st

# st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
# #CSS for styling
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #0E0E0E;
#         color: white;
#     }
#     .stTextInput>div>div>input {
#         background-color: #222;
#         color: white;
#         border-radius: 8px;
#         border: 1px solid #555;
#         padding: 10px;
#     }
#     .stButton>button {
#         background: linear-gradient(90deg, #ff512f, #dd2476);
#         color: white;
#         border-radius: 8px;
#         font-weight: bold;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         background: linear-gradient(90deg, #dd2476, #ff512f);
#         transform: scale(1.05);
#     }
#     .stSlider>div>div {
#         background-color: #222 !important;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# #check password strength
# def check_password_strength(password):
#     score = 0
#     suggestions = []
#     entropy = calculate_entropy(password)

#     COMMON_PASSWORDS = {"password", "123456", "qwerty", "password123", "abc123", "letmein", "admin", "welcome"}

#     if password.lower() in COMMON_PASSWORDS:
#         return "❌ Weak", "This password is too common. Choose a stronger one."

#     length_ok = len(password) >= 8
#     upper_ok = re.search(r'[A-Z]', password)
#     lower_ok = re.search(r'[a-z]', password)
#     digit_ok = re.search(r'\d', password)
#     special_ok = re.search(r'[!@#$%^&*]', password)

#     if length_ok: score += 1
#     else: suggestions.append("Increase password length to at least 8 characters.")

#     if upper_ok and lower_ok: score += 1
#     else: suggestions.append("Include both uppercase and lowercase letters.")

#     if digit_ok: score += 1
#     else: suggestions.append("Add at least one numeric digit (0-9).")

#     if special_ok: score += 1
#     else: suggestions.append("Include at least one special character (!@#$%^&*).")

#     if score == 5:
#         return "✅ Strong", f"Your password is strong! Entropy: {entropy:.2f} bits"
#     elif score >= 3:
#         return "⚠️ Moderate", f"Your password is decent, but consider these improvements:\n- {'\n- '.join(suggestions)}\nEntropy: {entropy:.2f} bits"
#     else:
#         return "❌ Weak", f"Your password is weak. Suggestions:\n- {'\n- '.join(suggestions)}\nEntropy: {entropy:.2f} bits"

# def calculate_entropy(password):
#     char_space = sum([
#         26 if re.search(r'[a-z]', password) else 0,
#         26 if re.search(r'[A-Z]', password) else 0,
#         10 if re.search(r'\d', password) else 0,
#         8 if re.search(r'[!@#$%^&*]', password) else 0
#     ])
#     return math.log2(char_space) * len(password) if char_space else 0

# #generate a strong password
# def generate_password(length=12, use_special=True):
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#     if use_special:
#         chars += "!@#$%^&*"
#     return "".join(random.choice(chars) for _ in range(length))

# # Streamlit UI
# st.title("🔐 Password Strength Meter")

# if "password" not in st.session_state:
#     st.session_state["password"] = ""
# if "confirm_password" not in st.session_state:
#     st.session_state["confirm_password"] = ""

# password = st.text_input("Enter your password", type="password").strip()
# confirm_password = st.text_input("Confirm your password", type="password").strip()

# if st.button("Check Strength"):
#     if not password:
#         st.warning("⚠️ Please enter a password to check.")
#     elif password != confirm_password:
#         st.error("❌ Passwords do not match. Please try again.")
#     else:
#         strength, feedback = check_password_strength(password)
#         st.subheader(f"Strength: {strength}")
#         st.write(feedback)

# # Password generator section
# st.subheader("🔑 Need a strong password?")
# password_length = st.slider("Choose password length:", min_value=8, max_value=32, value=12)
# include_special = st.checkbox("Include special characters (!@#$%^&*)", value=True)

# if st.button("Generate Strong Password"):
#     strong_password = generate_password(password_length, include_special)
#     st.text_input("Generated Password:", strong_password, key="generated_password")

import re
import random
import math
import streamlit as st

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🔧 Options")
    if st.button("Reset Fields"):
        st.session_state["password"] = ""
        st.session_state["confirm_password"] = ""
        st.session_state["generated_password"] = ""
        st.rerun()

    st.subheader("About")
    st.info("🔐 This app helps you check your password strength and generate strong passwords.")

# CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #0E0E0E;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #222;
        color: white;
        border-radius: 8px;
        border: 1px solid #555;
        padding: 10px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff512f, #dd2476);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #dd2476, #ff512f);
        transform: scale(1.05);
    }
    .stSlider>div>div {
        background-color: #222 !important;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []
    entropy = calculate_entropy(password)

    COMMON_PASSWORDS = {"password", "123456", "qwerty", "password123", "abc123", "letmein", "admin", "welcome"}

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Weak", "This password is too common. Choose a stronger one."

    length_ok = len(password) >= 8
    upper_ok = re.search(r'[A-Z]', password)
    lower_ok = re.search(r'[a-z]', password)
    digit_ok = re.search(r'\d', password)
    special_ok = re.search(r'[!@#$%^&*]', password)

    if length_ok: score += 1
    else: suggestions.append("Increase password length to at least 8 characters.")

    if upper_ok and lower_ok: score += 1
    else: suggestions.append("Include both uppercase and lowercase letters.")

    if digit_ok: score += 1
    else: suggestions.append("Add at least one numeric digit (0-9).")

    if special_ok: score += 1
    else: suggestions.append("Include at least one special character (!@#$%^&*).")

    if score == 5:
        return "✅ Strong", f"Your password is strong! Entropy: {entropy:.2f} bits"
    elif score >= 3:
        return "⚠️ Moderate", f"Your password is decent, but consider these improvements:\n- {'\n- '.join(suggestions)}\nEntropy: {entropy:.2f} bits"
    else:
        return "❌ Weak", f"Your password is weak. Suggestions:\n- {'\n- '.join(suggestions)}\nEntropy: {entropy:.2f} bits"

# Function to calculate entropy
def calculate_entropy(password):
    char_space = sum([
        26 if re.search(r'[a-z]', password) else 0,
        26 if re.search(r'[A-Z]', password) else 0,
        10 if re.search(r'\d', password) else 0,
        8 if re.search(r'[!@#$%^&*]', password) else 0
    ])
    return math.log2(char_space) * len(password) if char_space else 0

# Function to generate a strong password
def generate_password(length=12, use_special=True):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    if use_special:
        chars += "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

if "password" not in st.session_state:
    st.session_state["password"] = ""
if "confirm_password" not in st.session_state:
    st.session_state["confirm_password"] = ""
if "generated_password" not in st.session_state:
    st.session_state["generated_password"] = ""

password = st.text_input("Enter your password", type="password", key="password").strip()
confirm_password = st.text_input("Confirm your password", type="password", key="confirm_password").strip()

if st.button("Check Strength"):
    if not password:
        st.warning("⚠️ Please enter a password to check.")
    elif password != confirm_password:
        st.error("❌ Passwords do not match. Please try again.")
    else:
        strength, feedback = check_password_strength(password)
        st.subheader(f"Strength: {strength}")
        st.write(feedback)

# Password generator section
st.subheader("🔑 Need a strong password?")
password_length = st.slider("Choose password length:", min_value=8, max_value=32, value=12)
include_special = st.checkbox("Include special characters (!@#$%^&*)", value=True)

if st.button("Generate Strong Password"):
    st.session_state["generated_password"] = generate_password(password_length, include_special)

st.text_input("Generated Password:", st.session_state["generated_password"], key="generated_password_display")
