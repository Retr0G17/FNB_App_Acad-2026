# Countdown using a while loop

count = 4

while count >0:
    print(count)
    count -= 1
print("BLAST OFF !!!")


#Simple web counter using a for loop with range

for rep in range(1, 4):
    print(f'This is rep number: {rep}. ')

# Combining loops with conditions/decision making
#Guessing game

secret_word = "python"

while True: 
    guess = input("Guess the programming language used here: ").lower()

    if guess == secret_word:
        print("Congratulations! You guessed it right.")
        break

    else :
        print('Try Again!')
