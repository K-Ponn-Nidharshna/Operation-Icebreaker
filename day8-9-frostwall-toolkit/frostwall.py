import hashlib
import json
import os
import re
import pandas as pd

# ============================================================
#   FROSTWALL TOOLKIT — Operation IceBreaker
#   K. Ponn Nidharshna 
# ============================================================

HASH_STORE = "hash_store.json"
THRESHOLD = 3

COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567890", "iloveyou",
    "welcome", "login", "passw0rd", "master", "hello"
]

# ============================================================
#   TOOL 1 — FILE INTEGRITY CHECKER
# ============================================================

def compute_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def save_hash(filepath):
    hash_value = compute_hash(filepath)
    store = load_store()
    store[filepath] = hash_value
    with open(HASH_STORE, "w") as f:
        json.dump(store, f, indent=4)
    print(f"\n[✔] Hash saved for: {filepath}")
    print(f"    SHA-256: {hash_value}")

def check_integrity(filepath):
    store = load_store()
    if filepath not in store:
        print(f"\n[!] No hash found for: {filepath}")
        print("    Run option 1 first to save the hash.")
        return
    original_hash = store[filepath]
    current_hash = compute_hash(filepath)
    if original_hash == current_hash:
        print(f"\n[✔] File is CLEAN — no tampering detected.")
    else:
        print(f"\n[✘] WARNING — File has been TAMPERED with!")
        print(f"    Original : {original_hash}")
        print(f"    Current  : {current_hash}")

def load_store():
    if not os.path.exists(HASH_STORE):
        return {}
    with open(HASH_STORE, "r") as f:
        return json.load(f)

def file_integrity_menu():
    print("\n--- File Integrity Checker ---")
    print("1. Save file hash")
    print("2. Check file integrity")
    print("3. Back to main menu")
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice == "1":
            filepath = input("Enter file path: ").strip()
            if os.path.exists(filepath):
                save_hash(filepath)
            else:
                print("[!] File not found.")
        elif choice == "2":
            filepath = input("Enter file path: ").strip()
            if os.path.exists(filepath):
                check_integrity(filepath)
            else:
                print("[!] File not found.")
        elif choice == "3":
            break
        else:
            print("[!] Invalid choice.")

# ============================================================
#   TOOL 2 — PASSWORD STRENGTH CHECKER
# ============================================================

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        print("\n[✘] This is a very common password — immediately rejected!")
        return

    if len(password) >= 12:
        score += 2
        feedback.append("✔ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("~ Acceptable length (8+ characters)")
    else:
        feedback.append("✘ Too short (minimum 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✔ Contains uppercase letters")
    else:
        feedback.append("✘ Add uppercase letters (A-Z)")

    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✔ Contains lowercase letters")
    else:
        feedback.append("✘ Add lowercase letters (a-z)")

    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✔ Contains numbers")
    else:
        feedback.append("✘ Add numbers (0-9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
        feedback.append("✔ Contains special characters")
    else:
        feedback.append("✘ Add special characters (!@#$...)")

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

def password_menu():
    print("\n--- Password Strength Checker ---")
    while True:
        password = input("\nEnter password to check (or 'back' to exit): ")
        if password.lower() == "back":
            break
        check_password_strength(password)

# ============================================================
#   TOOL 3 — LOG ANALYZER
# ============================================================

def parse_log(filepath):
    records = []
    with open(filepath, "r") as f:
        for line in f:
            if "Failed login attempt" in line:
                match = re.search(
                    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) Failed login attempt from (\S+) user: (\S+)",
                    line
                )
                if match:
                    records.append({
                        "timestamp": match.group(1),
                        "ip_address": match.group(2),
                        "username": match.group(3)
                    })
    return pd.DataFrame(records)

def analyze_log(df):
    if df.empty:
        print("[!] No failed login attempts found.")
        return
    ip_counts = df.groupby("ip_address").size().reset_index(name="failed_attempts")
    ip_counts = ip_counts.sort_values("failed_attempts", ascending=False)
    print(f"\n[+] Total failed login attempts: {len(df)}")
    print(f"[+] Unique IPs involved: {df['ip_address'].nunique()}")
    print("\n--- Failed Attempts by IP ---")
    print(ip_counts.to_string(index=False))
    suspicious = ip_counts[ip_counts["failed_attempts"] >= THRESHOLD]
    print(f"\n--- Suspicious IPs (>= {THRESHOLD} attempts) ---")
    if suspicious.empty:
        print("[✔] No suspicious IPs detected.")
    else:
        for _, row in suspicious.iterrows():
            print(f"[⚠] {row['ip_address']} — {row['failed_attempts']} failed attempts — possible brute force!")

def log_menu():
    print("\n--- Log Analyzer ---")
    filepath = input("Enter log file path: ").strip()
    if os.path.exists(filepath):
        df = parse_log(filepath)
        analyze_log(df)
    else:
        print("[!] Log file not found.")

# ============================================================
#   MAIN MENU
# ============================================================

def main():
    while True:
        print("\n" + "=" * 50)
        print("   FROSTWALL TOOLKIT — Operation IceBreaker")
        print("   K. Ponn Nidharshna | Glacien.ai")
        print("=" * 50)
        print("1. File Integrity Checker")
        print("2. Password Strength Checker")
        print("3. Log Analyzer")
        print("4. Exit")
        print("-" * 50)

        choice = input("Select tool (1/2/3/4): ").strip()

        if choice == "1":
            file_integrity_menu()
        elif choice == "2":
            password_menu()
        elif choice == "3":
            log_menu()
        elif choice == "4":
            print("\nFrostwall secured. Stay frosty! 🧊")
            break
        else:
            print("[!] Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
