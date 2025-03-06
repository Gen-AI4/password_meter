# 🔐 Password Strength Meter

## 📌 Overview
This is a **Password Strength Meter** built using **Streamlit**. It evaluates the strength of user-provided passwords based on length, character diversity, and entropy. Additionally, it allows users to generate strong passwords.

## 🚀 Features
- **Password Strength Analysis**
  - Checks for length, uppercase/lowercase letters, digits, and special characters.
  - Provides entropy calculation.
  - Suggests improvements for weak passwords.

- **Password Confirmation**
  - Ensures both entered passwords match before evaluation.

- **Password Generator**
  - Generates strong passwords with customizable length.
  - Option to include special characters.

- **User-Friendly Interface**
  - Stylish UI with a dark theme.
  - Interactive sidebar for quick actions.

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/password-strength-meter.git
cd password-strength-meter
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Usage
Run the application with:
```bash
streamlit run app.py
```

## 📌 Sidebar Options
- **Reset Fields**: Clears all input fields.
- **Customize Password Generator**: Adjust password length and special character inclusion.

## 📷 Screenshot
![Password Strength Meter UI](screenshot.png)

## 🤝 Contributing
Feel free to open issues or submit pull requests to enhance functionality!

## 📝 License
This project is licensed under the **MIT License**.

