#Problem 7-1
#Ask the user for their favorite restaurant
favorite_restaurant = input("What is your favorite restaurant? ")

#Print a message that states the name of the restaurant
print("Let me help you find the closest " + favorite_restaurant)

#Problem 7-2
#Ask the user for two numbers
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

#Multiply the two numbers together
product = number1 * number2

#Print the result
print(f"The product of the two numbers is {product}")

#Problem 7-3
#Declare an empty list to store dinner items
dinner_items = []

#Ask the user for their dinner items
dinner_item = input("Enter a item you are planning to have for dinner or enter q to stop: ")

#If the user's response is not 'q', append the item to the list
if dinner_item != 'q':
    dinner_items.append(dinner_item)
    
#Declare a while loop to continue filling the user's dinner items
while dinner_item != 'q':
    dinner_item = input("Enter a item you are planning to have for dinner or enter q to stop: ")
    if dinner_item != 'q':
        dinner_items.append(dinner_item)
        
#Unless the user didn't enter any items, print the list of dinner items
if len(dinner_items) > 0:
    print("The items you are planning to have for dinner are: ")
    for dinner_item in dinner_items:
        print(dinner_item)

#Problem 7-4
#Ask the user for the carnival ride they want to ride
carnival_ride = input("What carnival ride would you like to ride? Press f for ferris wheel, t for tilt-a-whirl, p for pirate ship, or enter q to quit ")

#Determine the carnival ride the user wants to ride
if carnival_ride == "f":
    print("Pleasy pay $2.00 for the ferris wheel.")
elif carnival_ride == "t":
    print("Please pay $3.00 for the tilt-a-whirl.")
elif carnival_ride == "p":
    print("Please pay $3.50 for the pirate ship.")
elif carnival_ride != "q":
    print("This ride wasn't found. Please try again. ")

#Declate a while loop to continue until the user enters q
while carnival_ride != "q":
    carnival_ride = input("What carnival ride would you like to ride? Press f for ferris wheel, t for tilt-a-whirl, p for pirate ship, or enter q to quit ")
    if carnival_ride == "f":
        print("Pleasy pay $2.00 for the ferris wheel.")
    elif carnival_ride == "t":
        print("Please pay $3.00 for the tilt-a-whirl.")
    elif carnival_ride == "p":
        print("Please pay $3.50 for the pirate ship.")
    elif carnival_ride != "q":
        print("This ride wasn't found. Please try again. ")

#Problem 7-5
#Declare a list of grocery items
grocery_items = ["milk", "eggs", "bread", "cheese", "chicken", "eggs"]

#Loop through the instance of eggs in the list and remove it from the grocery list
count = 0
while count < len (grocery_items):
    if grocery_items[count] == "eggs":
        grocery_items.remove("eggs")
    count += 1
    
#Print out the remaining grocery items
print(grocery_items)
