# Tracking individual letters
name = 'python'

print(name[0])
print(name[-1])
print(name[2])

#string methods

town = 'Johannesburg'

print(town.upper())
print(town.lower())
print(town.strip())

#Creating a professional email generator

first = input("What is your first name? ")
last = input("What is your last name? ")

username = f"{first[0]}{last}"
print(f"Your email address is: {username.lower()}@fnb.app.academy.co.za")