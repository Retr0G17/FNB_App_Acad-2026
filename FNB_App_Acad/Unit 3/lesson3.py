#python basic arithmetic operations 

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#Displayed results using data type conversion and formatted strings

print(f'Your numbers added are: {int(num1) + int(num2)}') #addition
print(f'Your numbers subtracted are: {int(num2) - int(num1)}') #subtraction
print(f'Your numbers multiplied are: {int(num1) * int(num2)}') #multiplication
print(f'Your numbers divided are: {round(int(num1) / int(num2), 2)}') #division

bill = float(input("Enter the bill amount: R "))
tip = 0.15 * bill #tip calculation
total = bill + tip #total calculation

print(f'Your tip amount is: R {tip}') #display tip amount
print(f'Your total amount is: R {round(total, 2)}') #display total amount


#Unit 3 Challenge: fuel cost calculator

distance = float(input("Enter the distance to be traveled (km): "))
fuel_price = float(input("Enter the fuel price per liter (R): "))

fuel_efficiency = distance / 10

total_cost = fuel_efficiency * fuel_price

print(f'The total fuel cost for the trip is: R {round(total_cost, 2)}') #display total fuel cost

