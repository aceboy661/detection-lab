# Improved Failed Login Detector
# Now includes timestamps and better alerting

from datetime import datetime

def detect_failed_logins(log_file):
    failed_count = 0
    failed_entries = []

    try:
        with open(log_file, "r") as file:
            for line in file:
                if "Failed password" in line or "authentication failure" in line:
                    failed_count += 1
                    failed_entries.append(line.strip())

        print("=" * 50)
        print("FAILED LOGIN DETECTION REPORT")
        print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

        if failed_entries:
            print("\nDetected Failed Login Attempts:\n")
            for entry in failed_entries:
                print(f"- {entry}")

        print("\n" + "-" * 50)
        print(f"Total Failed Login Attempts: {failed_count}")

        if failed_count >= 5:
            print("ALERT: Possible brute-force attack detected!")
            print("Recommendation: Investigate source IP and consider blocking it.")
        elif failed_count > 0:
            print("Status: Some failed logins found (below alert threshold).")
        else:
            print("Status: No failed login attempts detected.")

        print("=" * 50)

    except FileNotFoundError:
        print("Error: Log file not found.")

# Run the detector
detect_failed_logins("logs/sample_auth.log")
