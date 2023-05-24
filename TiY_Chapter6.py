#Problem 6-1
#Declare dictionary for favorite movie
favorite_movie = {"title": "The Matrix", 
                  "movie_rating": "R",
                  "director": "The Wachowski Brothers",
                  "year": 1999, 
                  "genre": "Sci-Fi",
                  "user_rating": "8.7/10"}

#Problem 6-2
#Declare dictionary for chosen product
chosen_product = {"item_number": "6834",
                  "product_name": "Apple iPhone 6s",
                  "price": 799.99}

#Multiply price by 1.30
chosen_product["price"] *= 1.30

#print a message that the price of the item has increased by 30%
print(f"{chosen_product['product_name']}'s price has increased in price by 30% to ${chosen_product['price']}")

#Problem 6-3
#Declare for loop to loop through the items in the dictionary created in 6-1
for key, value in favorite_movie.items():
    print(f"{key}: {value}")

#Problem 6-4
#Declare a list of 3 dictionary items with each item containing a work and its definition
dictionary_items = [{"word": "Python", "Definition": "A programming language"},
                    {"word": "List", "Definition": "A collection of items in a particular order"},
                    {"word": "Variable", "Definition": "A placeholder for a value that can change"}]

#Declare an increment variable
count = 0

#Declare for loop to loop through the list of dictionary items
for word in dictionary_items:
    for key, value in dictionary_items[count].items():
        print(f"{key}: {value}")
    count += 1

#Problem 6-5
#Using the dictionary from 6-1, add a key to it that stores a list of actors/actresses who starred in the movie
favorite_movie = {"title": "The Matrix", 
                  "movie_rating": "R",
                  "director": "The Wachowski Brothers",
                  "year": 1999, 
                  "genre": "Sci-Fi",
                  "user_rating": "8.7/10",
                  "actors/actresses": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"]}

#Each out on their own line, loop through the list of actors/actresses and print them out
for actor in favorite_movie["actors/actresses"]:
    print(actor)