#Practical Task Lesson 1

# Student Information
# Collect and Display student information such as name, age, and favorite number.

name = input("What is your fullname and surname? ")
age = int(input('How old are you? '))
favorite_number = float(input('What is your favorite number? '))

print(f'Welcome, {name}')

print(name.upper())

print(name.title())

print( age * 12)

print(round(favorite_number, 2))

print(type(name), type(age), type(favorite_number))

#Unit 1 Challenge

name = input("What is your name? ")
artist = input("Who is your favorite artist? ")

print(f'Hey {name}! Your tickets to see {artist} are ready!')
