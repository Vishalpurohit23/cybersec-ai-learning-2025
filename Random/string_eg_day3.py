# Step 1: Ask for a statement
statement = input("Enter your statement: ")

# Step 2: Print index and corresponding letter
print("\n📍 Index and Letters:")
for index, letter in enumerate(statement):
    print(f"{index}: {letter}")

# Step 3: Reverse each word and capitalize the first letter of the reversed word
words = statement.split()

# Reverse each word and capitalize its first letter
reversed_words = [word[::-1].capitalize() for word in words]

# Join the transformed words into a final statement
reversed_statement = ' '.join(reversed_words)

print("\n🔁 Reversed Words with Capitalized First Letters:")
print(reversed_statement)

# ==================================================================================================================

# Explanation!!!!!

'''Step 2: Print index and letters
print("\n📍 Index and Letters:")


👶 What this does:
- It tells the computer: “Hey! Let’s start showing each letter in the sentence, one by one.”
- \n is like pressing Enter—it makes a new line so things don’t look squished.
- The 📍 emoji is just decoration. Like stickers on your notebook!

for index, letter in enumerate(statement):
    print(f"{index}: {letter}")


👶 Let’s break this down:
- Imagine your sentence is a long train 🚂 made of letters.
- enumerate(statement) is like counting each train car:
- The first car is number 0, the second is 1, and so on.
- Each car also has a letter inside it.
So if your sentence is "Hi", the computer sees:
0: H
1: i


- for index, letter in ... means:
- “Let’s look at each car one by one.”
- index is the car number.
- letter is the letter inside the car.
- print(f"{index}: {letter}") tells the computer:
- “Say the number of the car, then say the letter inside it.”
It’s like saying:
“Car number 0 has the letter H!”


🔵 Step 3: Reverse each word and make the first letter big
words = statement.split()


👶 What this does:
- It takes your whole sentence and chops it into words.
- Like cutting a sandwich into pieces 🍞🍞🍞.
- "I love Python" becomes ['I', 'love', 'Python']

reversed_words = [word[::-1].capitalize() for word in words]


👶 This is the magic part!
Let’s look at it piece by piece:
🧩 word[::-1]
- This flips the word backwards.
- Like turning the word around in a mirror 🪞.
- "python" becomes "nohtyp"
🧩 .capitalize()
- This makes the first letter big and the rest small.
- "nohtyp" becomes "Nohtyp"
🧩 [ ... for word in words ]
- This is like saying:
- “Do this trick for every word in the sentence!”

So if your sentence is "hello world", it becomes:
['olleH', 'dlroW']



reversed_statement = ' '.join(reversed_words)


👶 What this does:
- It takes all the reversed words and glues them back together with spaces.
- Like putting puzzle pieces back into a line 🧩🧩🧩.
- ['olleH', 'dlroW'] becomes "olleH dlroW"

print("\n🔁 Reversed Words with Capitalized First Letters:")
print(reversed_statement)


👶 Final step:
- Show the new sentence to the user!
- It’s like saying:
“Ta-da! Here’s your sentence with each word flipped and looking fancy!”
'''
