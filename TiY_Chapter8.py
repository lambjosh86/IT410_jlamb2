#Problem 8-1
#Define the favorite radio station
def tune_in_radio_station(radio_station):
    print("Let me tune in " + radio_station)

#Ask the user for their favorite radio station
radio_station = input("What is your favorite radio station? ")

#Call the function and pass the user's favorite radio station
tune_in_radio_station(radio_station)

#Problem 8-2
#Define the business card function
def print_business_cards(name, quantity, tag_line):
    print(f"Printing {quantity} business cards for {name} with the tag line {tag_line}")

#Call the function three times with different arguments
print_business_cards("Outback Steakhouse", 500, "No rules, just right")
print_business_cards("Applebee's", 1000, "Eatin' good in the neighborhood")
print_business_cards("Chili's", 250, "I want my baby back, baby back, baby back")

#Problem 8-3
#Define the business card function, but with a default quantity of 100
def print_business_cards(name, tag_line, quantity=100):
    print(f"Printing {quantity} business cards for {name} with the tag line {tag_line}")
    
#Call the rewritten function two times with different arguments. One time by passing a quantity of 150 and the other time by not passing a quantity
print_business_cards("Outback Steakhouse", "No rules, just right", 150)
print_business_cards("Applebee's", "Eatin' good in the neighborhood")

#Problem 8-4
#Define the function that accepts song information specific to song title and artist
def song_information(song_title, artist_name="Unknown"):
    formatted_song_information = f"{song_title} by {artist_name}"
    return formatted_song_information

#Call the function three times with one of the calls not passing an artist name
song_information("The Middle", "Jimmy Eat World")
song_information("Boulevard of Broken Dreams")
song_information("Girlfriend", "Avril Lavigne")

#Problem 8-5
#Re-define the function that accepts song information specific to song title and artist
def song_information(song_title, artist_name="Unknown"):
    dictionary_item = {"title": song_title, "artist": artist_name}
    return song_information

#Define the function that prints song entries in a playlist
def print_song_entries(playlist):
    print("The following songs are in the playlist: ")
    for song in playlist:
        print(song)
        
#Create an empty playlist
playlist = []

#Using a while loop, add songs to the playlist
while True:
    song_title = input("Enter a song title or enter q to quit: ")
    if song_title == "q":
        break
    artist_name = input("Enter the artist name: ")
    song = song_information(song_title, artist_name)
    playlist.append(song)
    
#Print the playlist
print_song_entries(playlist)
