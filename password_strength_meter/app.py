from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    password = None

    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)

    return render_template("index.html", strength=strength, password=password)

if __name__ == "__main__":
    app.run(debug=True)