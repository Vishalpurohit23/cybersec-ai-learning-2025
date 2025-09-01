# list to hold usernames of locked admin accounts
import csv
import os
locked_admin_accounts = []


# Open the csv file with user account data
# __file__ is a special variable that holds the path to the current script file.
# os.path.abspath(__file__) converts that to an absolute path (no .. or relative parts).
# os.path.dirname(...) strips off the filename, leaving only the directory path.


script_dir = os.path.dirname(os.path.abspath(
    __file__))   # folder where script is saved
file_path = os.path.join(script_dir, "accounts.csv")

with open(file_path, mode="r") as f:
    reader = csv.DictReader(f)

    # process each account row
    for row in reader:
        # check if the account is admin and locked
        if row["account_type"] == "admin" and row["is_locked"].lower() == "true":
            locked_admin_accounts.append(row["username"])

with open("locked_admins_report.txt", "w")as r:
    r.write("Locked Admin Account Report: \n")
    r.write("---------------------------------- \n")

    for username in locked_admin_accounts:
        r.write(username + "\n")
print(
    f"Audit Complete.Found {len(locked_admin_accounts)} locked admin accounts in the file.")
print("Report saved to  'locked_admins_report.txt'")
