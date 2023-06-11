#Declare the Person class
class Person():
    """Define the Person class"""
    def __init__(self, name, email_address):
        """Initialize the attributes of the Person class"""
        self.name = name
        self.email_address = email_address

#Declare the Student class
class Student(Person):
    """Define the Student class"""
    def __init__(self, name, email_address, student_ID, program_of_study):
        """Initalize the attributes of the Student class"""
        super().__init__(name, email_address)
        self.student_ID = student_ID
        self.program_of_study = program_of_study

    def __str__(self):
        """This method is defined to display the student's information"""
        return f"Name: {self.name.title()}\nEmail: {self.email_address}\nStudent ID Number: {self.student_ID}\nProgram of Study: {self.program_of_study.title()}"

#Declare the Instructor class
class Instructor(Person):
    """Define the Instructor class"""
    def __init__(self, name, email_address, instructor_ID, institution_graduated_from, highest_degree):
        """Initialize the attributes of the Instructor class"""
        super().__init__(name, email_address)
        self.instructor_ID = instructor_ID
        self.institution_graduated_from = institution_graduated_from
        self.highest_degree = highest_degree
        
    def __str__(self):
        """This method is defined to display the instructor's information"""
        return f"Name: {self.name.title()}\nEmail: {self.email_address}\nInstructor ID Number: {self.instructor_ID}\nLast Institution: {self.institution_graduated_from.title()}\nHighest Degree Earned: {self.highest_degree.title()}"
 
#Declare the Validator class which will utilize different methods to validate the information entered by the user
class Validator():
    def __init__(self):
        """This constructor method is empty as there are no real attributes"""
        
    #Declare the validateEmail method which will validate the email address entered by the user
    def validateEmail(self, email):
        """This method will validate the email address entered by the user"""
        forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
        #Check if the email address contains any forbidden characters
        for character in forbidden_characters_email:
            if character in email:
                return False
        return True
    
    def validateStudentID(self, student_ID):
        #Check if the student ID contains only digits and is less than or equal to 7 digits. If it does, return True. Otherwise, return False
        return student_ID.isdigit() and len(student_ID) <= 7
    
    def validateInstructorID(self, instructor_ID):
        #Check if the instructor ID contains only digits and is less than or equal to 5 digits. If it does, return True. Otherwise, return False
        return instructor_ID.isdigit() and len(instructor_ID) <= 5
        
    def validateName(self, name):
        """This method will validate the name entered by the user"""
        forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
        forbidden_characters_found = False
        #Check if the name contains any forbidden characters
        for character in forbidden_characters_name:
            if character in name:
                return False
            return True
        
#Delare the empty college records list
college_records = []
#Declare the variable that will be used to continue the program
continue_program = True

def studentInformation():
    validator = Validator()
    """This function will prompt the user to enter the student's information"""
    valid_student_name = False
    while not valid_student_name:
        #Prompt the user to enter the student's name
        student_name = input("Enter the student's name: ")
        if validator.validateName(student_name):
            #If the name is valid, break the loop
            valid_student_name = True
        else:
            #If the name is invalid, print an error message and ask the user to enter a valid name
            print("The name was not formatted correctly. Please try again.")

    valid_student_email = False
    while not valid_student_email:
        #Prompt the user to enter the student's email address
        student_email = input("Enter the student's email address: ")
        if validator.validateEmail(student_email):
            #If the email address is valid, break the loop
            valid_student_email = True
        else:
            #If the email address is invalid, print an error message and ask the user to enter a valid email address
            print("The email address was not formatted correctly. Please try again.")
            
    valid_student_ID = False
    while not valid_student_ID:
        #Prompt the user to enter the student's ID number
        student_ID = input("Enter the student's ID number (7 or less digits): ")
        if validator.validateStudentID(student_ID):
            #If the student ID is valid, break the loop
            valid_student_ID = True
        else:
            #If the student ID is invalid, print an error message and ask the user to enter a valid student ID
            print("The student ID was not formatted correctly. Please try again.")
            
    valid_program_of_study = False
    while not valid_program_of_study:
        #Prompt the user to enter the student's program of study
        program_of_study = input("Enter the student's program of study: ")
        #Check if the program of study is alphabetical. If it is, return True. Otherwise, return False
        if program_of_study.isalpha():
            #If the program of study is valid, break the loop
            valid_program_of_study = True
        else:
            #If the program of study is invalid, print an error message and ask the user to enter a valid program of study
            print("The program of study was not formatted correctly. Please try again.")
        #Create a student object of the Student class and return it
        return Student(student_name, student_email, student_ID, program_of_study)
    
def instructorInformation():
    validator = Validator()
    """This function will prompt the user to enter the instructor's information"""
    valid_instructor_name = False
    while not valid_instructor_name:
        #Prompt the user to enter the instructor's name
        instructor_name = input("Enter the instructor's name: ")
        if validator.validateName(instructor_name):
            #If the name is valid, break the loop
            valid_instructor_name = True
        else:
            print("The name was not formatted correctly. Please try again.")
            
    valid_instructor_email = False
    while not valid_instructor_email:
        #Prompt the user to enter the instructor's email address
        instructor_email = input("Enter the instructor's email address: ")
        if validator.validateEmail(instructor_email):
            #If the email address is valid, break the loop
            valid_instructor_email = True
        else:
            print("The email address was not formatted correctly. Please try again.")
            
    valid_instructor_ID = False
    while not valid_instructor_ID:
        #Prompt the user to enter the instructor's ID number
        instructor_ID = input("Enter the instructor's ID number (5 or less digits): ")
        if validator.validateInstructorID(instructor_ID):
            #If the instructor ID is valid, break the loop
            valid_instructor_ID = True
        else:
            print("The instructor ID was not formatted correctly. Please try again.")
            
    valid_institution_graduated_from = False
    while not valid_institution_graduated_from:
        #Prompt the user to enter the last institution the instructor graduated from
        institution_graduated_from = input("Enter the last institution the instructor graduated from: ")
        if institution_graduated_from.isalpha():
            #If the institution is valid, break the loop
            valid_institution_graduated_from = True        
        else:
            print("The institution was not formatted correctly. Please try again.")
            
    valid_highest_degree_earned = False
    while not valid_highest_degree_earned:
        #Prompt the user to enter the highest degree the instructor has earned
        highest_degree_earned = input("Enter the highest degree the instructor has earned: ")
        #Check if the highest degree earned is alphabetical. If it is, return True. Otherwise, return False
        if highest_degree_earned.isalpha():
            #If the highest degree earned is valid, break the loop
            valid_highest_degree_earned = True
        else:
            print("The highest degree earned was not formatted correctly. Please try again.")
        #Create an instructor object of the Instructor class and return it
        return Instructor(instructor_name, instructor_email, instructor_ID, institution_graduated_from, highest_degree_earned)
    
while continue_program:
    """This function will prompt the user to enter a student or instructor's information, or to quit the program"""
    user = input("Enter 's' to enter a student's information, 'i' to enter an instructor's information, or 'q' to quit the program: ")
    if user.lower() == "s":
        college_records.append(studentInformation())
    elif user.lower() == "i":
        college_records.append(instructorInformation())
    elif user.lower() == "q":
        #If the user enters "q", end the program
        continue_program = False
        
#Display the college records list after the user has entered all of the records desired during the session
print("Here are the college records entered during this session: ")
for record in college_records:
#Print a blank line for formatting purposes
    print()
    print(record)