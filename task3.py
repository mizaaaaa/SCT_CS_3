import tkinter as tk
import re

class PasswordChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Strength Checker")
        self.root.configure(bg="white")  # White background
        self.root.resizable(False, False)

        window_width = 500
        window_height = 370
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.show_password = False

        # Title
        tk.Label(root, text="🔐 Password Checker", font=("Calibri", 18, "bold"),
                 fg="#000000", bg="white").pack(pady=(15, 5))

        # Step 1: Password input
        tk.Label(root, text="Step 1: Enter Password", font=("Calibri", 12),
                 fg="#333333", bg="white").pack()

        self.input_frame = tk.Frame(root, bg="white")
        self.input_frame.pack(pady=10)

        self.entry = tk.Entry(self.input_frame, width=30, font=("Calibri", 13),
                              show="*", justify="center", relief="solid",
                              bg="#f0f0f0", fg="#000000", insertbackground="black")
        self.entry.grid(row=0, column=0, ipady=6, padx=(0, 5))

        self.toggle_btn = tk.Button(self.input_frame, text="👁", font=("Calibri", 12),
                                    width=3, command=self.toggle_password,
                                    bg="#f0f0f0", fg="black", relief="flat", bd=0)
        self.toggle_btn.grid(row=0, column=1)

        # Step 2: Buttons
        self.button_frame = tk.Frame(root, bg="white")
        self.button_frame.pack(pady=20)

        tk.Button(self.button_frame, text="✅ Check Strength", font=("Calibri", 12, "bold"),
                  bg="#00c853", fg="white", activebackground="#00b248", relief="flat",
                  command=self.evaluate, width=20, pady=5).grid(row=0, column=0, padx=10)

        tk.Button(self.button_frame, text="🧹 Clear", font=("Calibri", 12, "bold"),
                  bg="#d50000", fg="white", activebackground="#b71c1c", relief="flat",
                  command=self.clear, width=20, pady=5).grid(row=0, column=1, padx=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Calibri", 11),
                                     fg="#01579b", bg="white", justify="left", wraplength=450)
        self.result_label.pack(pady=10)

    def toggle_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            self.entry.config(show="")
            self.toggle_btn.config(text="🙈")
        else:
            self.entry.config(show="*")
            self.toggle_btn.config(text="👁")

    def evaluate(self):
        password = self.entry.get()
        if not password:
            self.custom_popup("Input Error", "Please enter a password")
            return

        strength, feedback = self.check_strength(password)
        result_text = f"🔒 Password Strength: {strength}"

        if feedback:
            result_text += "\n\n🛠 Suggestions:\n- " + "\n- ".join(feedback)

        self.result_label.config(text=result_text)

    def check_strength(self, password):
        feedback = []

        if len(password) < 8:
            feedback.append("Too short (min 8 characters).")
        if re.search(r"[a-z]", password) is None:
            feedback.append("Missing lowercase letters.")
        if re.search(r"[A-Z]", password) is None:
            feedback.append("Missing uppercase letters.")
        if re.search(r"\d", password) is None:
            feedback.append("Missing digits.")
        if re.search(r"[^A-Za-z0-9]", password) is None:
            feedback.append("Missing special characters.")

        score = 5 - len(feedback)

        if score == 5 and len(password) >= 12:
            strength = "💪 Very Strong"
        elif score >= 4:
            strength = "✔ Strong"
        elif score == 3:
            strength = "⚠ Medium"
        elif score == 2:
            strength = "❗ Weak"
        else:
            strength = "🚫 Very Weak"

        return strength, feedback

    def clear(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

    def custom_popup(self, title, message):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x150")
        popup.configure(bg="white")
        popup.resizable(False, False)

        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 150
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 75
        popup.geometry(f"+{x}+{y}")

        tk.Label(popup, text=title, font=("Calibri", 14, "bold"), fg="#d50000", bg="white").pack(pady=(20, 5))
        tk.Label(popup, text=message, font=("Calibri", 12), fg="#333333", bg="white", wraplength=250).pack()

        tk.Button(popup, text="OK", command=popup.destroy, font=("Calibri", 11, "bold"),
                  bg="#e53935", fg="white", activebackground="#c62828", relief="flat", padx=10).pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordChecker(root)
    root.mainloop()
