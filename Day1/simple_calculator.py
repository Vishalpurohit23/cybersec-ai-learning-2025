
import math
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The sum of {num1} and {num2} is: {num1 + num2}")
print(f"The difference of {num1} and {num2} is: {num1 - num2}")
print(f"The product of {num1} and {num2} is: {num1 * num2}")
print(
    f"The quotient of {num1} and {num2} is: {num1 / num2 if num2 != 0 else 'undefined'}")
print(f"The modulus of {num1} and {num2} is: {num1 % num2}")
print(
    f"The exponentiation of {num1} to the power of {num2} is: {num1 ** num2}")
print(
    f"The floor division of {num1} by {num2} is: {num1 // num2 if num2 != 0 else 'undefined'}")
print(f"The absolute value of {num1} is: {abs(num1)}")
print(f"The absolute value of {num2} is: {abs(num2)}")
print(f"The maximum of {num1} and {num2} is: {max(num1, num2)}")
print(f"The minimum of {num1} and {num2} is: {min(num1, num2)}")
print(f"The square root of {num1} is: {num1 ** 0.5}")
print(f"The square root of {num2} is: {num2 ** 0.5}")
print(f"The logarithm of {num1} is: {math.log(num1)}")
print(f"The logarithm of {num2} is: {math.log(num2)}")
