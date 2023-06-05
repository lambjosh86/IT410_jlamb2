#Define a function to determine if the employee ID is correct
def employee_ID_correct(employee_ID):
    return len(employee_ID) <= 7 and employee_ID.isdigit()

#Define a function to determine if the employee's name is correct
def employee_name_correct(employee_name):
    #Declare the forbidden characters for the employee's name
    forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}']
    #Validate that the employee's name is correct
    for character in forbidden_characters_name:
        if character in employee_name:
            return False
    return True

#Define a function to determine if the employee's email address is correct
def employee_email_correct(employee_email):
    #Declare the forbidden characters for the employee's email address
    forbidden_characters_email = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
    #Validate that the employee's email address is correct
    for character in forbidden_characters_email:
        if character in employee_email:
            return False
    return True

#Define a function to determine if the employee's address is correct
def employee_address_correct(employee_address):
    #Declare the forbidden characters for the employee's address
    forbidden_characters_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
    #Validate that the employee's address is correct
    for character in forbidden_characters_address:
        if character in employee_address:
            return False
    return True

#Define a function to obtain the employee's ID
def obtain_employee_ID():
    while True:
        try:
            employee_ID = input("Please enter your employee ID: ")
            if employee_ID_correct(employee_ID):
                return employee_ID
            else:
                print("Employee ID was not formatted correctly. Please try again.")
        except:
            print("Employee ID was not formatted correctly. Please try again.")

#Define a function to obtain the employee's name
def obtain_employee_name():
    while True:
        employee_name = input("Please enter your employee name: ")
        if employee_name_correct(employee_name):
            return employee_name
        else:
            print("Employee name was not formatted correctly. Please try again. ")
            
#Define a function to obtain the employee's email address
def obtain_employee_email():
    while True:
        employee_email = input("Please enter your email address: ")
        if employee_email_correct(employee_email):
            return employee_email
        else:
            print("Employee email was not formatted correctly. Please try again. ")
            
#Define a function to obtain the employee's address
def obtain_employee_address():
    while True:
        employee_address = input("Please enter the employee's home address(optional): ")
        if employee_address_correct(employee_address):
            return employee_address
        else:
            print("Employee address was not formatted correctly. Please try again. ")

#Create an empty list to store the employee's information
employee_data = []

#Declare a variable to count the number of employees entered into the system
count = 0

#Obtain the employee's information
while count < 5:
    employee_ID = obtain_employee_ID()
    employee_name = obtain_employee_name()
    employee_email = obtain_employee_email()
    employee_address = obtain_employee_address()
    
    #Append employee data to the dictionary
    #If the employee's home address field was left blank or invalid, the if statement will be executed
    #If the employee's home address field was not left blank, the else statement will be executed
    if employee_address == '':
        employee_data.append({"Employee ID": employee_ID,"Name": employee_name.title(), "Email": employee_email})
    else:
        employee_data.append({"Employee ID": employee_ID,"Name": employee_name.title(), "Email": employee_email, "Home Address": employee_address.title()})
        
    #Prompt the user if they would like to enter another employee's information
    #If the user types "N", the loop will break and, the program will print the dictionary
    #If the user types "Y", they will be prompted to enter another employee's information
    enter_another_employee = input("Would you like to enter another employee's information? (Y/N): ")
    if enter_another_employee == "N":
        break
    else:
        enter_another_employee = "Y"
        count += 1
        continue

#Print the dictionary
print("Here are the employee(s) that you entered into the database: ")
print(employee_data)