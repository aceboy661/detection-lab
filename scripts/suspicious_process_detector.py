# Suspicious Process Detector
# Looks for processes running from unusual locations

def detect_suspicious_processes(log_file):
    suspicious_count = 0
    suspicious_paths = ["/tmp/", "/dev/shm/", "/var/tmp/"]

    try:
        with open(log_file, "r") as file:
            for line in file:
                for path in suspicious_paths:
                    if path in line:
                        suspicious_count += 1
                        print(line.strip())

        print("-----------------------------")
        print("Total suspicious process events:", suspicious_count)

        if suspicious_count >= 1:
            print("ALERT: Suspicious process activity detected!")
        else:
            print("No suspicious processes found.")

    except FileNotFoundError:
        print("Error: Log file not found.")

detect_suspicious_processes("logs/sample_process.log")
