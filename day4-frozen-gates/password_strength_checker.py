import re

COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567890", "iloveyou",
    "welcome", "login", "passw0rd", "master", "hello"
]

def check_password_strength(password):
    score = 0
    feedback = []

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        print("\n[✘] This is a very common password — immediately rejected!")
        return

    # Length check
    if len(password) >= 12:
        score += 2
        feedback.append("✔ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("~ Acceptable length (8+ characters)")
    else:
        feedback.append("✘ Too short (minimum 8 characters)")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✔ Contains uppercase letters")
    else:
        feedback.append("✘ Add uppercase letters (A-Z)")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✔ Contains lowercase letters")
    else:
        feedback.append("✘ Add lowercase letters (a-z)")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✔ Contains numbers")
    else:
        feedback.append("✘ Add numbers (0-9)")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
        feedback.append("✔ Contains special characters")
    else:
        feedback.append("✘ Add special characters (!@#$...)")

    # Result
    print("\n--- Password Strength Report ---")
    for item in feedback:
        print(f"  {item}")

    print(f"\n  Score: {score}/7")

    if score >= 6:
        print("  Strength: STRONG 💪")
    elif score >= 4:
        print("  Strength: MODERATE ⚠")
    else:
        print("  Strength: WEAK ✘")

def main():
    print("=" * 45)
    print("   PASSWORD STRENGTH CHECKER — Operation IceBreaker")
    print("=" * 45)

    while True:
        password = input("\nEnter password to check (or 'quit' to exit): ")
        if password.lower() == "quit":
            print("Exiting. Stay frosty!")
            break
        check_password_strength(password)

if __name__ == "__main__":
    main()


