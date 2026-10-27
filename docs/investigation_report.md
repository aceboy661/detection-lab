# Investigation Report - Failed Login & Suspicious Process Activity

**Date:** October 27, 2026  
**Analyst:** Marlon Lonmon  
**Project:** Host-Based Detection Lab

---

## Summary
Two detection scripts were executed against sample host logs. Both triggered alerts indicating potentially malicious activity.

---

## Finding 1: Possible Brute-Force Attack

**Detection Script:** failed_login_detector.py  
**Log Source:** sample_auth.log

**Details:**
- 6 failed login attempts detected in a short time window
- Targeted accounts: admin, root, test
- Source IP: 192.168.1.50

**Severity:** Medium  
**Recommendation:** Block the source IP and review account lockout policies.

---

## Finding 2: Suspicious Process Execution

**Detection Script:** suspicious_process_detector.py  
**Log Source:** sample_process.log

**Details:**
- Processes were launched from unusual locations:
  - /tmp/
  - /dev/shm/
  - /var/tmp/
- These locations are commonly used by malware and attackers

**Severity:** High  
**Recommendation:** Investigate the affected host, terminate suspicious processes, and check for persistence mechanisms.

---

## Conclusion
The detection scripts successfully identified suspicious activity. This demonstrates basic detection engineering and log analysis skills relevant to a SOC Tier 1 role.
