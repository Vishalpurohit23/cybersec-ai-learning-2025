# Day 2 Basics: Variables, Types, Lists, and Simple Loops

# Variables and types
user_count = 3                  # int
rotation_days = 90              # int
service_account = True          # bool
platform = "Windows"            # str
threshold = 0.85                # float

print(type(user_count), type(platform), type(service_account), type(threshold))

# Type conversion (e.g., input returns str)
age_str = "42"
age = int(age_str)              # str -> int
print(age + 1)

# Lists (sequence of items)
users = ["alice.adm", "bob.svc", "carol"]
print("Total users:", len(users))
print("First user:", users[0])

# Append and extend
users.append("dave")
users.extend(["eve", "frank"])
print("Updated users:", users)

# Loop through list
for u in users:
    print("Processing:", u)

# List slicing
core_users = users[:3]      # first 3
last_two = users[-2:]       # last 2
print("Core:", core_users, "| Last two:", last_two)

# Basic string formatting (f-strings)
for u in users:
    print(f"User {u} has platform: {platform}")

# Simple safeguards
if len(users) > 0:
    print("Users list not empty.")
else:
    print("Users list is empty.")
