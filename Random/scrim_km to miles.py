# this is user input excercise provided by Scrimba
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name


user = input("Enter your first name: ")
km = float(input("Enter the distance in kilometers: "))
miles = km / 1.609
print(f"Hello {user.capitalize()}, the distance in kilometers is {round(km, 1)} km, which is {round(miles, 1)} miles.")
# - Did you use f-string for printing the output? yes!!
# - Did you capitalize the name? yes!!
# - Did you use correct types for calculating and printing? float
