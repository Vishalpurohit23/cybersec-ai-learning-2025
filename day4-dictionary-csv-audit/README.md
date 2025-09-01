 #Day 4 - Python Dictionaries & CSV File Audit

## Overview
This project demonstrates how to automate a common cybersecurity task: auditing user accounts. The Python script reads account data from a `accounts.csv` file, simulating a data export from a system like CyberArk or Active Directory.

## Functionality Practiced
- **Python Dictionaries:** Storing and accessing multi-attribute data for each account.
- **CSV File Reading:** Using Python's built-in `csv` module to parse structured data.
- **Conditional Logic:** Filtering accounts based on specific criteria (e.g., `account_type` and `is_locked` status).
- **File Writing:** Generating a clean, readable audit report (`locked_admins_report.txt`).

## How to Use
1.  Ensure `accounts.csv` and `account_audit_csv.py` are in the same directory.
2.  Run the script from your terminal: `python account_audit_csv.py`
3.  The script will generate `locked_admins_report.txt` with a list of all admin accounts that are locked.

## Why This Matters
This skill is crucial for automating compliance checks, security audits, and operational tasks in a Privileged Access Management (PAM) or Identity and Access Management (IAM) role. It saves significant manual effort and reduces human error.
