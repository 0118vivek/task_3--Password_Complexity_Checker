import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>?/]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")

    # Assess overall strength
    if strength == 5:
        return "Strong Password 💪", feedback
    elif strength >= 3:
        return "Moderate Password 😐", feedback
    else:
        return "Weak Password ❌", feedback

# Get user input
password = input("Enter a password: ")
strength, suggestions = check_password_strength(password)

# Display results
print("\nPassword Strength:", strength)
if suggestions:
    print("Suggestions to improve:")
    for suggestion in suggestions:
        print("-", suggestion)
