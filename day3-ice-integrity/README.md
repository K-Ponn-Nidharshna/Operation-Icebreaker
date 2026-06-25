# Day 3 — Ice Integrity: File Integrity Checker
**Operation IceBreaker | K. Ponn Nidharshna**

## What This Tool Does
Detects if a file has been tampered with by comparing its 
current SHA-256 hash against a previously saved hash.

## Hashing vs Encryption

- **Hashing** is a one-way process — you cannot reverse a hash 
  back to the original data. Used to verify integrity.
- **Encryption** is reversible — data can be decrypted with 
  the right key. Used to protect confidentiality.
- Passwords are hashed (not encrypted) so that even if a 
  database is stolen, the actual passwords cannot be recovered.

## How to Run
python file_integrity_checker.py

## How to Use
1. Choose option 1 — enter a file path to save its hash
2. Modify the file (or leave it unchanged)
3. Choose option 2 — check if the file was tampered with

## Technologies Used
- Python 3
- hashlib (SHA-256)
- json (hash storage)






