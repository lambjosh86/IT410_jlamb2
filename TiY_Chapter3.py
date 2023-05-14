#Problem 3-1
books = ["The Hobbit", "The Lord of the Rings", "The Silmarillion", "The Children of Hurin"]
print("I just read:", books[0].title())
print("I just read:", books[1].title())
print("I just read:", books[2].title())
print("I just read:", books[3].title())

#Problem 3-2
favorite_shows = ["Gotham Knights", "The Simpsons", "The Flash", "South Park"]
favorite_shows[0] = "The Mandalorian"
favorite_shows.append("Wednesday")
favorite_shows.insert(2, "Stranger Things")
popped_show = favorite_shows.pop(3)
print(popped_show)
del favorite_shows[0:3]
print(favorite_shows)

#Problem 3-3
favorite_games = ["The Legend of Zelda", "Super Mario Bros.", "Minecraft", "Pokemon"]
print(len(favorite_games))
favorite_games.sort()
print(favorite_games)
print(sorted(favorite_games))
favorite_games.reverse()
print(favorite_games)

#Problem 3-4
shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
print(shopping_list[4])

#shopping_list = ["Milk", "Eggs", "Bread", "Butter", "Cheese"]
#print(shopping_list[4])