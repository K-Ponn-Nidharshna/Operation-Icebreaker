import pandas as pd
import re

LOG_FILE = "sample_auth.log"
THRESHOLD = 3  # flag IPs with 3+ failed attempts

def parse_log(filepath):
    records = []
    with open(filepath, "r") as f:
        for line in f:
            if "Failed login attempt" in line:
                # Extract timestamp, IP, and user
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

def analyze(df):
    print("=" * 50)
    print("   LOG ANALYZER — Operation IceBreaker")
    print("=" * 50)

    if df.empty:
        print("[!] No failed login attempts found.")
        return

    # Group by IP
    ip_counts = df.groupby("ip_address").size().reset_index(name="failed_attempts")
    ip_counts = ip_counts.sort_values("failed_attempts", ascending=False)

    print(f"\n[+] Total failed login attempts: {len(df)}")
    print(f"[+] Unique IPs involved: {df['ip_address'].nunique()}")

    print("\n--- Failed Attempts by IP ---")
    print(ip_counts.to_string(index=False))

    # Flag suspicious IPs
    suspicious = ip_counts[ip_counts["failed_attempts"] >= THRESHOLD]

    print(f"\n--- Suspicious IPs (>= {THRESHOLD} attempts) ---")
    if suspicious.empty:
        print("[✔] No suspicious IPs detected.")
    else:
        for _, row in suspicious.iterrows():
            print(f"[⚠] {row['ip_address']} — {row['failed_attempts']} failed attempts — possible brute force!")

def summary(df):
    print("\n--- What I Found in the Log ---")
    print(f"  • Log entries analyzed: {len(df)}")
    suspicious = df.groupby("ip_address").size()
    suspicious = suspicious[suspicious >= THRESHOLD]
    print(f"  • Suspicious IPs flagged: {len(suspicious)}")
    for ip, count in suspicious.items():
        print(f"    → {ip} tried {count} times — likely brute force attack")
    print("\n  Recommendation: Block these IPs at the firewall immediately.")

def main():
    df = parse_log(LOG_FILE)
    analyze(df)
    summary(df)

if __name__ == "__main__":
    main()
