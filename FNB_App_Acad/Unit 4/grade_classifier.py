# Practical task 
#Student grade classifier

lname = input("Enter your name: ")
subject1 = float(input("Enter your first subject's grade: "))
subject2 = float(input("Enter your second subject's grade: "))
subject3 = float(input("Enter your third subject's grade: "))

average = (subject1 + subject2 + subject3) / 3

if average >= 80:
    print('A, You have passed')
elif average >=70 and average <=79:
    print('B, You have passed')
elif average >=60 and average <=69:
    print('C, You have passed')
elif average >=50 and average <=59:
    print('D, You have passed')
else:
    print('F, You have failed')

    if subject1 < 40 or subject2 < 40 or subject3 < 40:
        print('Needs intervention in 1 or more subjects.')

