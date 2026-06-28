# Day 6 — Tracks in the Snow: Log Analyzer
**Operation IceBreaker | K. Ponn Nidharshna**

## What This Tool Does
Reads a server authentication log, detects failed login 
attempts, groups them by IP address, and flags IPs 
that show signs of brute force attacks.

## What I Found in the Log
- 192.168.1.105 — 5 failed attempts — likely brute force
- 203.0.113.42 — 5 failed attempts — likely brute force
- 198.51.100.77 — 2 failed attempts — suspicious

## Key Concepts
- **IP Address** — unique address identifying a device on a network
- **Auth Log** — a record of all login attempts on a server
- **Brute Force** — repeatedly trying passwords until one works
- **Threshold** — minimum number of failures to flag as suspicious

## How to Run
pip install pandas
python log_analyzer.py

## Technologies Used
- Python 3
- Pandas (data analysis)
- re (regular expressions)


