#Problem 4-1
favorites_places = ["New York", "Los Angeles", "Chicago", "Miami"]
for favorite_place in favorites_places:
    print(favorite_place + " is a nice place to visit.")

#Problem 4-2
for value in range(90, 101):
    print(value)

#Problem 4-3
numbers = list(range(100000, 1000001))
print(sum(numbers))

#Problem 4-4
numbers = [1, 34, 2, 4, 21, 3, 45, 5, 76, 11, 10, 12, 13, 16, 20, 17, 14, 19, 15, 18]
print(max(numbers))
print(min(numbers))

#Problem 4-5
multiples_of_five = list(range(5, 101, 5))
print(multiples_of_five)

#Problem 4-6
twenty_to_thirty = list(range(20, 31))
print(twenty_to_thirty)
twenty_to_thirty = [value * 2 for value in twenty_to_thirty]
print(twenty_to_thirty)

#Problem 4-7
#Printing the first 2 values
print(numbers[0:2])
#Printing items 5-10
print(numbers[4:10])
#Printing the last 4 values
print(numbers[-4:])

#Problem 4-8
favorite_bands = ["Linkin Park", "Green Day", "The Beatles"]
fav_bands = favorite_bands[:]
favorite_bands.append("The Rolling Stones")
print(favorite_bands)
print(fav_bands)

#Problem 4-9
grades = ("1st", "2nd", "3rd", "4th", "5th")
grades[0] = "6th"
