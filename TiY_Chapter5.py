#Problem 5-1
#I predict the expression will evaluate to True
car = 'subaru'
print(car == 'subaru')

#I predict the expression will evaluate to True
division = 10/2
print(division == 5)

#I predict the expression will evaluate to True
color = 'light blue'
print(color == 'light blue')

#I predict the expression will evaluate to False
temperature = 100
print(temperature < 32)

#I predict the expression will evaluate to False
age = 21
print(age == 18)

#I predict the expression will evaluate to False
favorite_number = 7
print(favorite_number == 3)

#Problem 5-2
number1 = 4
if number1 % 2 == 1:
    print("Number 4 is odd.")
number2 = 1
if number2 % 2 == 1:
    print("Number 1 is odd.")

#Problem 5-3
#Test with an even number
if number1 % 2 == 1:
    print("Number 4 is odd.")
else:
    number1 = number1 + 1
    print(f"{number1} is odd.")
#Test with an odd number    
if number2 % 2 == 1:
    print("Number 1 is odd.")
else:
    number2 = number2 + 1
    print(f"{number2} is odd.")
    
#Problem 5-4
favorite_fruits = ['apples', 'bananas', 'grapes']

if len(favorite_fruits) == 2:
    print("I like two fruits")
elif len(favorite_fruits) == 3:
    print("I like three fruits")
elif len(favorite_fruits) == 4:
    print("I like four fruits")
else:
    print("I like several fruits")
    
#Problem 5-5
#Declare a list of numbers
numbers = list(range(1,56))

#Declare two number variables
number1 = 44
number2 = 55

#loop through the list of numbers and check if number 44 is in the list
if number1 in numbers:
        print(f"{number1} was found.")
else:
        print(f"{number1} was not found.")
        
#loop through the list of numbers and check if number 55 is in the list
if number2 in numbers:
        print(f"{number2} was found.")
else:  
        print(f"{number2} was not found.")
        
#Problem 5-6
#Declare of list of favorite stores and another list of stores that are running sales
favorite_stores = ['Target', 'Walmart', 'Kroger', 'Publix', 'Costco']
sales_stores = ['Target', 'Walmart', 'Kroger']

#Loop through the list of favorite stores and check if the store is running a sale
for store in favorite_stores:
    if store in sales_stores:
        print(f"{store} is currently running a sale.")
    else:
        print(f"{store} isn't currently running a sale.")