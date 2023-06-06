#Problem 9-1
class Shirt():
    """A class to represent a shirt"""  
    def __init__(self, size, color):
        """Initialize the shirt attributes"""
        self.size = size
        self.color = color

    def print_size_and_color(self):
        """Print the size and color attributes"""
        print("The shirt is a size " + self.size)
        print("The shirt is " + self.color)
        
my_shirt = Shirt("large", "blue")
print("The attributes of my shirt are: ")
print(my_shirt.size)
print(my_shirt.color)
my_shirt.print_size_and_color()

Your_shirt = Shirt("medium", "red")
print("The attributes of your shirt are: ")
print(Your_shirt.size)
print(Your_shirt.color)
Your_shirt.print_size_and_color()
        


#Problem 9-2


#Problem 9-3


#Problem 9-4

