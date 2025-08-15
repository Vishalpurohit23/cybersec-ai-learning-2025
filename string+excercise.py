# From the String "Welcome to Python 101: Strings", extract text and create/ print a new string that says
# *"1 Welcom Ring to Tyler"
# Every first letter in a word should be capitalized (title format)
# then print the same string backwords
text = "Welcome to Python 101: Strings"
msg = 'welcome to Python 101: Strings'
#       012345678910111213141516171819

# print('"' + text[18] + text.capitalize()[0:7] + text.capitalize() + [25] + text[8:11] + text[12:16] + text[17:18] + text[19:] + '"')
print(f'"{text[-10].upper() + text[0:7]} {text[-5].capitalize()}{text[-4]}{text[-3]}{text[-2]} {text[-6].capitalize()}{text[9]} {text[13].capitalize()}{text[12]}{text[2]}{text[1]}{text[-5]} "')
print(f"{text[::-1]}")
# this is working!!!!!


# you can use this instead,this is a more readable and better way to do it


# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
# print(msg1.title())
# print the string in title format (capitalizing the first letter of each word)
