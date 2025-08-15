# Create a new file generate_userlist.py.

# Use this script to create a file with new usernames:
# Step 1: no need to import notepad but for csv Import the CSV module
# This module helps us work with textfile easily

usernames = ["jdoe", "asmith", "blim", "ftan", "kpatel"]
with open("userlist_temp.txt", "w") as file:
    for user in usernames:
        file.write(user + "\n")
        # You can add more user details here if needed
        # For example:
        # file.write(f"{user}, {age}, {location}\n")
    print("User list written to userlist_temp.txt.")
