#Declare the Person class
class Person():
    """This class will extend into the Student and Instructor classes"""
    def __init__(self, name, email_address, individual_ID):
        """Initialize name, email_address, and individual_ID attributes of the Person class"""
        self.name = name
        self.email_address = email_address
        self.individual_ID = individual_ID

#Declare the Student class which inherits from the Person class and stores the student records
class Student(Person):
    """This will store the student's records"""
    def __init__(self, name, email_address, student_ID, program_of_study):
        """Initalize the attributes of the Student class"""
        super().__init__(name, email_address, student_ID)
        self.program_of_study = program_of_study
    def displayInformation(self):
        """This will display the student's information"""
        print(f"{self.name.title()}'s email address is {self.email_address}. Their student ID is {self.individual_ID}. Their program of study is {self.program_of_study}.")

#Declare the Instructor class which inherits from the Person class and stores the instructor records
class Instructor(Person):
    """This will store the instructor's records"""
    def __init__(self, name, email_address, instructor_ID, institution_graduated_from, highest_degree):
        """Initialize the attributes of the Instructor class"""
        super().__init__(name, email_address, instructor_ID)
        self.institution_graduated_from = institution_graduated_from
        self.highest_degree = highest_degree
    def displayInformation(self):
        """This will display the instructor's information"""
        print(f"{self.name.title()}'s email address is {self.email_address}. Their instructor ID is {self.individual_ID}. The last institution they graduated from is {self.institution_graduated_from} and their highest degree is {self.highest_degree}.")
 
#Declare the Validator class which will utilize different methods to validate the information entered by the user
class Validator():
    def __init__(self):
        """This constructor method is empty as there are no real attributes"""
        
    def validateEmail(self, email):
        """This method will validate the email address entered by the user"""
        forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
        forbidden_characters_found = False
        #Check if the email address contains any forbidden characters
        for character in forbidden_characters_email:
            if character in email:
                forbidden_characters_found = True
                break
        #If forbidden characters are found, return False. Otherwise, return True
        if forbidden_characters_found == True or len(email) == 0:
            return False
        else:
            return True
        
    def validateIndividualID(self, individual_ID, maxLength):
        """This method will validate the individual ID entered by the user"""
        #If the individual ID includes anything other than numbers or is longer than the max length of 5, return False. Otherwise, return True
        numerical_digit_test = individual_ID.isdigit()
        if numerical_digit_test == False or len(individual_ID) > maxLength:
            return False
        else:
            return True
        
    def validateName(self, name):
        """This method will validate the name entered by the user"""
        forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\','0','1','2','3','4','5','6','7','8','9']
        forbidden_characters_found = False
        #Check if the name contains any forbidden characters
        for character in forbidden_characters_name:
            if character in name:
                forbidden_characters_found = True
                break
        #If forbidden characters are found, return False. Otherwise, return True
        if forbidden_characters_found == True or len(name) == 0:
            return False
        else:
            return True
        
#Delare the empty college records list
college_records = []

#Declare the outer while loop control variable
add_another_user = "yes"

#Declare the outer while loop. If the user enters "q" after inputting a record, the loop will break
while add_another_user != "q":
    #Start the individualType loop which will continue until the user enters a valid input of either "S" for student or "I" for instructor
    while True:
        individualType = input("Are you entering a student or an instructor? Enter 'S' for student or 'I' for instructor: ").lower()
        if individualType == "s" or individualType == "i":
            break
        else:
            print("The type of individual was not formatted correctly. Please try again.")
            
    #Delare a person object of the Validator class that will be used to validate the user's different inputs
    person = Validator()
    
    #Start the name loop which will continue until the user enters a valid name
    while True:
        name = input("Enter the name of the individual: ")
        #Call the validateName method of the Validator class to validate the name. If the name is false, we will prompt the user to enter a valid name, otherwise we will break the loop
        valid_name = person.validateName(name)
        if valid_name == False:
            print("The name was not formatted correctly. Please try again.")
        else:
            break
    
    #Start the email loop which will continue until the user enters a valid email address
    while True:
        email_address = input("Enter the email address of the individual: ")
        #Call the validateEmail method of the Validator class to validate the email address. If the email address is false, we will prompt the user to enter a valid email address, otherwise we will break the loop
        valid_email = person.validateEmail(email_address)
        if valid_email == False:
            print("The email address was not formatted correctly. Please try again.")
        else:
            break
    
    #If the user is entering a student, we will prompt them to enter the student ID and program of study
    if individualType == "s":
    
        #Start the student ID loop which will continue until the user enters a valid student ID
        while True:
            student_ID = input("Enter the student ID of the individual: ")
            #Call the validateIndividualID method of the Validator class to validate the student ID. If the student ID is false, we will prompt the user to enter a valid student ID, otherwise we will break the loop
            valid_student_ID = person.validateIndividualID(student_ID, 7)
            if valid_student_ID == False:
                print("The student ID was not formatted correctly. Please try again.")
            else:
                break
        
        #Start the program of study loop which will continue until the user enters a valid program of study
        while True:
            program_of_study = input("Enter the program of study of the student: ")
            #If the program of study is empty, we will prompt the user to enter a valid program of study, otherwise we will break the loop
            if len(program_of_study) == 0:
                print("The program of study is required. Please try again.")
            else:
                break
        
        #Create a student object of the Student class after the user has entered all of the required information. Append the student object to the college records list and call the displayInformation method of the Student class to display the student's information
        student = Student(name, email_address, student_ID, program_of_study)
        college_records.append(student)
        college_records.append(student.email_address)
        college_records.append(student.student_ID)
        college_records.append(student.program_of_study)
        student.displayInformation()
        
    #If the user is entering an instructor, we will prompt them to enter the instructor ID, graduate institution, and highest degree
    else:
        #Start the instructor ID loop which will continue until the user enters a valid instructor ID
        while True:
            instructor_ID = input("Enter the instructor ID of the individual: ")
            #Call the validateIndividualID method of the Validator class to validate the instructor ID. If the instructor ID is false, we will prompt the user to enter a valid instructor ID, otherwise we will break the loop
            valid_instructor_ID = person.validateIndividualID(instructor_ID, 5)
            if valid_instructor_ID == False:
                print("The instructor ID was not formatted correctly. Please try again.")
            else:
                break
        
        #Start the last institution graduated from loop which will continue until the user enters a valid last institution graduated from
        while True:
            institution_graduated_from = input("Enter the last institution graduated from of the instructor: ")
            #If the last institution graduated from is empty, we will prompt the user to enter a valid last institution graduated from, otherwise we will break the loop
            if len(institution_graduated_from) == 0:
                print("The last institution graduated from is required. Please try again.")
            else:
                break
        
        #Start the highest degree loop which will continue until the user enters a valid highest degree
        while True:
            highest_degree = input("Enter the highest degree of the instructor: ")
            #If the highest degree is empty, we will prompt the user to enter a valid highest degree, otherwise we will break the loop
            if len(highest_degree) == 0:
                print("The highest degree is required. Please try again.")
            else:
                break
        
        #Create an instructor object of the Instructor class after the user has entered all of the required information. Append the instructor object to the college records list and call the displayInformation method of the Instructor class to display the instructor's information
        instructor = Instructor(name, email_address, instructor_ID, institution_graduated_from, highest_degree)
        college_records.append(instructor.name)
        college_records.append(instructor.email_address)
        college_records.append(instructor.instructor_ID)
        college_records.append(instructor.institution_graduated_from)
        college_records.append(instructor.highest_degree)
        instructor.displayInformation()
        
        #If the user enters "q" after inputting a record, the loop will break. Otherwise, the user will be prompted to enter another record
        enter_another_record = input("Enter another record? Enter 'q' to quit or any other key to continue: ").lower()
        
        #Display the college records list after the user has entered all of the records desired during the session
        print("Here are the college records entered during this session: ")
        for record in college_records:
            print(record)