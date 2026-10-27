# Investigation Report - Host-Based Detection Lab

**Date:** October 27, 2026  
**Analyst:** Marlon Lonmon  
**Project:** Host-Based Detection Lab

---

## Summary
Three custom detection scripts were executed against sample host logs. Multiple alerts were triggered, indicating potentially malicious activity.

---

## Finding 1: Possible Brute-Force Attack

**Detection Script:** failed_login_detector.py  
**Log Source:** sample_auth.log

- 6 failed login attempts detected
- Targeted accounts: admin, root, test
- Source IP: 192.168.1.50

**Severity:** Medium  
**Recommendation:** Block the source IP and review account lockout policies.

---

## Finding 2: Suspicious Process Execution

**Detection Script:** suspicious_process_detector.py  
**Log Source:** sample_process.log

- Processes launched from unusual locations (/tmp/, /dev/shm/, /var/tmp/)
- These locations are commonly abused by malware

**Severity:** High  
**Recommendation:** Investigate the host, terminate suspicious processes, and check for persistence.

---

## Finding 3: Privilege Escalation Activity

**Detection Script:** privilege_escalation_detector.py  
**Log Source:** sample_privilege.log

- Multiple sudo, su, useradd, and usermod events detected
- Includes a failed su attempt and creation of a new user

**Severity:** High  
**Recommendation:** Verify if these actions were authorized. Review privileged account activity.

---

## Conclusion
The detection scripts successfully identified suspicious activity across authentication, process execution, and privilege escalation. This project demonstrates practical detection engineering and log analysis skills relevant to a SOC Tier 1 role.
