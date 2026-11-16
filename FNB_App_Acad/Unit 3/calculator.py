#Practical Task 3: Calculator
# Simple calculator program

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f'Your numbers added are: {round(num1 + num2, 2)}') #addition
print(f'Your numbers subtracted are: {round(num2 - num1, 2)}') #subtraction
print(f'Your numbers multiplied are: {round(num1 * num2, 2)}') #multiplication
print(f'Your numbers divided are: {round(num1 / num2, 2)}') #division

print(f'Your numbers raised to the power of each other are: {round(num1 ** num2, 2)}') #exponentiation
print(f'Your numbers modulo are: {round(num1 % num2, 2)}') #modulus
print(f'Your numbers floor division are: {round(num1 // num2, 2)}') #floor division

print(' Division by zero is allowed')

