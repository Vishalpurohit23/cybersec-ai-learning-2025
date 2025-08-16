# generate_userlist.py
# Goal: Generate a batch of usernames for onboarding and save them to a file

# We import the 'os' module to work with file paths and directories
import os


# Function: generate_usernames
# Purpose: Creates a list of usernames like jsmith01, jsmith02, etc.
# Parameters:
#   base  -> the starting text for the username (like 'jsmith')
#   count -> how many usernames to generate
#   start -> the number to start counting from (default = 1)
#   pad   -> how many digits to pad the number with (default = 2 → gives 01, 02, etc.)
def generate_usernames(base: str, count: int, start: int = 1, pad: int = 2):
    result = []  # an empty list that will store the generated usernames

    # Loop through numbers from 'start' up to 'start + count - 1'
    for i in range(start, start + count):
        # Convert the number i into a string, padded with zeros
        # Example: if i=1 and pad=2 → "01"
        suffix = str(i).zfill(pad)

        # Combine the base with the padded number
        # Example: base = "jsmith", suffix = "01" → "jsmith01"
        result.append(f"{base}{suffix}")

    return result  # return the full list of usernames back to the caller


# Function: save_lines
# Purpose: Save a list of strings (usernames) to a text file, one per line
def save_lines(filepath: str, lines: list):
    # 'with open()' ensures the file is opened and properly closed after use
    # "w" = write mode (overwrites existing file), encoding="utf-8" handles special characters
    with open(filepath, "w", encoding="utf-8") as f:
        # Loop through every username in the list and write it to the file
        for line in lines:
            # add newline at the end so each username is on its own line
            f.write(line + "\n")

# this line often confuses beginners, but it’s super important in Python.
# This block ensures the code only runs if the file is executed directly,
# and not if it's imported as a module into another program
# In Python, every file (script) has a special built-in variable called __name__.
# When you run a Python file directly, Python sets __name__ = "__main__".
# When you import that file into another program, Python sets __name__ to the file’s name instead.


if __name__ == "__main__":
    print("=== User List Generator ===")

    # Ask the user for the base username (e.g., "jsmith")
    base = input("Enter base username (e.g., jsmith): ").strip()

    # Ask how many usernames to generate (as a string initially)
    count_str = input("How many users to generate? ").strip()

    # Convert the count input into an integer safely
    try:
        count = int(count_str)  # convert string to integer
        if count <= 0:
            # We don’t allow zero or negative numbers
            raise ValueError("Count must be positive.")
    except ValueError:
        # If input is not a valid integer, show an error and exit the program
        print("Invalid count. Please enter a positive integer.")
        raise SystemExit(1)

    # Call our function to generate usernames
    usernames = generate_usernames(base, count)

    # Build the file path where usernames will be saved
    # os.getcwd() = current working directory
    # os is Python’s Operating System module (we imported it at the top).
    # File will be saved as "userlist.txt" in the current folder
    outfile = os.path.join(os.getcwd(), "userlist.txt")
# getcwd() means “get current working directory”.
# It takes care of slashes (/ on Linux/Mac, \ on Windows) so you don’t have to worry.
# We are storing the full file path into the variable outfile.

    # Save the usernames list to the file
    save_lines(outfile, usernames)

    # Print confirmation messages
    print(f"Created {len(usernames)} usernames.")
    print(f"Saved to: {outfile}")
