# Host-Based Detection Lab

A hands-on cybersecurity project focused on log analysis, detection engineering, and basic threat detection.

This project demonstrates practical skills relevant to SOC Analyst, Junior Cybersecurity Analyst, and IT Security roles.

## Project Overview

This lab simulates host-based detection by analyzing authentication logs and identifying suspicious activity such as brute-force attempts.

### Skills Demonstrated
- Log analysis
- Writing custom detection logic
- Python scripting for security
- Documentation and investigation notes
- Version control with Git & GitHub

## Project Structure

- logs/ → Sample log files
- scripts/ → Detection scripts
- detections/ → Detection rules and notes
- docs/ → Investigation reports
- README.md

## Current Detections

### 1. Failed Login Detector
- File: scripts/failed_login_detector.py
- Description: Analyzes authentication logs for failed login attempts.
- Alert Condition: 5 or more failed logins triggers an alert for possible brute-force activity.

## How to Run

python3 scripts/failed_login_detector.py

## Author
Marlon Lonmon  
GitHub: aceboy661
