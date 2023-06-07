#Problem 9-1
#Shirt class with attributes size and color
class Shirt_1():
    """A class to represent a shirt with size and color attributes"""  
    def __init__(self, size, color):
        """Initialize the shirt attributes"""
        self.size = size
        self.color = color

    def print_size_and_color(self):
        """Print the size and color attributes"""
        print("The shirt is a size " + self.size)
        print("The shirt is " + self.color)
        
#Create an instance of the Shirt class and print the attributes
shirt1 = Shirt_1("large", "blue")
print("The attributes of shirt one are: ")
print(shirt1.size)
print(shirt1.color)
shirt1.print_size_and_color()

#Create another instance of the Shirt class and print the attributes
shirt2 = Shirt_1("medium", "red")
print("The attributes of shirt two are: ")
print(shirt2.size)
print(shirt2.color)
shirt2.print_size_and_color()

#Problem 9-2
#New shirt class with a quantity attribute and increase/decrease methods
class Shirt_2():
    """A class to represent a shirt with size, color, and quantity attributes"""
    def __init__(self, size, color, quantity=1):
        """Initialize the different shirt attributes"""
        self.size = size
        self.color = color
        self.quantity = quantity
    def increase_quantity(self, value):
        """This method increases the quantity attribute of the shirt with a specified value"""
        self.quantity = self.quantity + value
    def decrease_quantity(self, value):
        """This method decreases the quantity attribute of the shirt with a specified value"""
        self.quantity = self.quantity - value
        
#Create an instance of the new shirt class, call the increase method three different times and decrease function twice using different numbers each time, and print the quantity attribute after each call
the_shirt2 = Shirt_2("large", "blue", 5)
the_shirt2.increase_quantity(2)
print(the_shirt2.quantity)
the_shirt2.increase_quantity(1)
print(the_shirt2.quantity)
the_shirt2.increase_quantity(3)
print(the_shirt2.quantity)
the_shirt2.decrease_quantity(5)
print(the_shirt2.quantity)
the_shirt2.decrease_quantity(6)
print(the_shirt2.quantity)
  
#Problem 9-3
#Clothing class with a quantity attribute and increase/decrease methods
class Clothing():
    """A class to represent a base class for different articles of clothing"""
    def __init__(self, size, color, quantity=1):
        """Initialize the different clothing attributes"""
        self.size = size
        self.color = color
        self.quantity = quantity
    def increase_quantity(self, value):
        """This method increases the quantity attribute of the clothing with a specified value"""
        self.quantity = self.quantity + value
    def decrease_quantity(self, value):
        """This method decreases the quantity attribute of the clothing with a specified value"""
        self.quantity = self.quantity - value
        
#Shirt class that inherits from the Clothing class
class ShirtInherit(Clothing):
    """A class to represent a shirt with additional type information and a printed message"""
    def __init__(self, size, color, quantity, type, message):
        """Initialize the ShirtInherit attributes"""
        super().__init__(size, color, quantity)
        self.type = type
        self.message = message
    def print_message(self):
        """Prints the message on the shirt"""
        print("The message on the shirt is: " + self.message)
        
#Create an instance of the ShirtInherit class
the_shirt3 = ShirtInherit("large", "blue", 5, "long-sleeve", "I love Python!")
the_shirt3.increase_quantity(2)
print(the_shirt3.quantity)
the_shirt3.print_message()

#Problem 9-4
#Pants class that inherits from the Clothing class
class Pants(Clothing):
    """A child class of the Clothing class to represent pants with additional fabric type and style attributes"""
    def __init__(self, size, color, quantity, fabric, style):
        """Initialize the Pants attributes"""
        super().__init__(size, color, quantity)
        self.fabric = fabric
        self.style = style
