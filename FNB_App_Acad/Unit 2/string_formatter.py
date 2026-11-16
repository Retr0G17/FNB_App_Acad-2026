#Practical Task
# Username and Message Formatter

fname = input('Enter your First Name: ')
lname = input('Enter your Last Name: ')

username = f"{fname[0]}{lname}"
print(f"Your username is: {username.lower()}")

fullname = f"{fname} {lname}"
print(fullname.title())

Bio = f"I am {fullname} and I am a registered participant of the FNB App Academy for the 2026 year. My username is {username.lower()} and I am excited to learn Python Programming."
print(Bio.strip() + str(Bio.__len__()) + Bio.replace('I am', "I'm") )

#Unit 2 Challenge

password = input('What is your password? ')

password = password.strip()


print(f"Your password hint: it starts with {password.upper()[0]} and end with {password.upper()[-1]}. ")
