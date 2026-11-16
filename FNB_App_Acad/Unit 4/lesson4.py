# Basic if/else statements

age = int(input('Enter your age: '))
selection_pass = input('Do you have a VIP ticket? (yes/no): ').lower()


if age >= 18 and selection_pass == 'yes':
    print('Access granted to the VIP section. ')
elif age >= 18:
    print('Access granted to the general section. ')
else : 
    print('Access denied, You are too young to enter the venue.')

# Unit 4 Challenge 
#Smart ATM Withdrawal simulator

balance = 500

withdrawal_amount = float(input('Enter the amount you want to withdraw: '))

if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f'Withdrawal successful. Your new balance is: ${balance:.2f}')

elif withdrawal_amount <= 0:
    print('Invalid withdrawal amount. You must withdraw more than R0.')

else:
    print('Declined. Insufficient funds for this withdrawal.')

