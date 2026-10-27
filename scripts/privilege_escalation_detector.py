# Privilege Escalation Detector
# Looks for potential privilege escalation activity in logs

from datetime import datetime

def detect_privilege_escalation(log_file):
    escalation_count = 0
    escalation_entries = []

    keywords = ["sudo", "su ", "useradd", "usermod", "passwd", "privilege"]

    try:
        with open(log_file, "r") as file:
            for line in file:
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        escalation_count += 1
                        escalation_entries.append(line.strip())
                        break

        print("=" * 50)
        print("PRIVILEGE ESCALATION DETECTION REPORT")
        print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

        if escalation_entries:
            print("\nPotential Privilege Escalation Events:\n")
            for entry in escalation_entries:
                print(f"- {entry}")

        print("\n" + "-" * 50)
        print(f"Total Potential Escalation Events: {escalation_count}")

        if escalation_count >= 1:
            print("ALERT: Possible privilege escalation activity detected!")
            print("Recommendation: Review the events and verify if they were authorized.")
        else:
            print("Status: No privilege escalation activity detected.")

        print("=" * 50)

    except FileNotFoundError:
        print("Error: Log file not found.")

# Run the detector
detect_privilege_escalation("logs/sample_privilege.log")
