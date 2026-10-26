def detect_failed_logins(log_file):
    failed_count = 0

    try:
        with open(log_file, "r") as file:
            for line in file:
                if "Failed password" in line:
                    failed_count += 1
                    print(line.strip())

        print("-----------------------------")
        print("Total failed login attempts:", failed_count)

        if failed_count >= 5:
            print("ALERT: Possible brute-force attack detected!")
        else:
            print("No suspicious activity detected.")

    except FileNotFoundError:
        print("Error: Log file not found.")

detect_failed_logins("logs/sample_auth.log")
