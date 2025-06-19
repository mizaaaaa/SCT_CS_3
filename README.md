# 🔐 Password Strength Checker

A simple and colorful Tkinter GUI application to check the strength of your passwords in real time. It analyzes your password for length, uppercase/lowercase letters, numbers, and special characters, and gives you feedback and suggestions to make your passwords stronger.

## Features

- **Modern UI:** Clean, user-friendly interface built with Tkinter.
- **Real-Time Feedback:** Evaluates password strength and provides actionable suggestions.
- **Show/Hide Password:** Toggle password visibility for easy input.
- **Clear Button:** Quickly reset the input and results.
- **Custom Popups:** User-friendly error messages for missing input.

## How It Works

1. **Enter your password** in the input box.
2. Click **"✅ Check Strength"** to evaluate your password.
3. View the strength rating and suggested improvements.
4. Use **"👁"** to show/hide your password.
5. Click **"🧹 Clear"** to reset and try another password.

## Password Strength Criteria

- **Minimum length:** 8 characters (12+ for "Very Strong")
- **Contains:** Lowercase, uppercase, digit, and special character
- **Strength Levels:**  
  - 💪 Very Strong  
  - ✔ Strong  
  - ⚠ Medium  
  - ❗ Weak  
  - 🚫 Very Weak


## Getting Started

### Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### How to Run

1. **Clone this repository:**
    ```bash
    git clone https://github.com/mizaaaaa/SCT_CS_3.git
    cd SCT_CS_3
    ```

2. **Run the application:**
    ```bash
    python task3.py
    ```

## File Structure

- `task3.py` — Main application code for the password strength checker.

## Customization

You can modify the password strength rules by editing the `check_strength` method in `task3.py`.

## License

This project is open-source and available under the MIT License.

---

**Enjoy creating stronger passwords!**
