import hashlib
import json
import os

HASH_STORE = "hash_store.json"

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
    print(f"[✔] Hash saved for: {filepath}")
    print(f"    SHA-256: {hash_value}")

def check_integrity(filepath):
    store = load_store()
    if filepath not in store:
        print(f"[!] No hash found for: {filepath}")
        print("    Run option 1 first to save the hash.")
        return
    original_hash = store[filepath]
    current_hash = compute_hash(filepath)
    if original_hash == current_hash:
        print(f"[✔] File is CLEAN — no tampering detected.")
    else:
        print(f"[✘] WARNING — File has been TAMPERED with!")
        print(f"    Original : {original_hash}")
        print(f"    Current  : {current_hash}")

def load_store():
    if not os.path.exists(HASH_STORE):
        return {}
    with open(HASH_STORE, "r") as f:
        return json.load(f)

def main():
    print("=" * 45)
    print("   FILE INTEGRITY CHECKER — Operation IceBreaker")
    print("=" * 45)
    print("1. Save file hash")
    print("2. Check file integrity")
    print("3. Exit")
    print("-" * 45)

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
            print("Exiting. Stay frosty!")
            break
        else:
            print("[!] Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
