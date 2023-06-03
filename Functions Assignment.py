
#Create an empty list to store the employee's information
employee_data = []

#Define the employee ID
def obtain_employee_ID():
    while True:
        try:
            #Obtain employee ID from user
            employee_ID = input("Please enter your employee ID: ")
            #Validate that the employee ID is correct
            if len(employee_ID) <= 7 and employee_ID.isdigit():
                #If the employee ID is correct, return the employee ID
                return employee_ID
            else:
                #If the employee ID is incorrect, provide an error message and prompt the user to enter their employee ID again
                print("Employee ID was not formatted correctly. Please try again.")
        except:
            print("Employee ID was not formatted correctly. Please try again.")

#Define the employee's name
def obtain_employee_name():
    while True:
            #Obtain the employee's name
            employee_name = input("Please enter your first name: ")
            #Declare the forbidden characters for the employee's name
            forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
            #Validate that the employee's name is correct
            if employee_name:
                if any(character in forbidden_characters_name for character in employee_name):
                    #If the employee's name is incorrect, provide an error message and prompt the user to enter their name again
                    print("Employee name was not formatted correctly. Please try again. ")
                else:
                    #If the employee's name is correct, return the employee's name
                    return employee_name
            else:
                print("Employee name was not formatted correctly. Please try again. ")
                
#Define the employee's email address
def obtain_employee_email():
    while True:
            #Obtain the employee's email address
            employee_email = input("Please enter your email address: ")
            Validate_Employee_Email = False
            #Declare the forbidden characters for the employee's email address
            forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
            #Validate that the employee's email address is correct
            if employee_email:
                if any(character in forbidden_characters_email for character in employee_email):
                    #If the employee's email address is incorrect, provide an error message and prompt the user to enter their email address again
                    print("Employee email was not formatted correctly. Please try again. ")
                else:
                    #If the employee's email address is correct, return the employee's email address
                    return employee_email
            else:
                print("Employee email was not formatted correctly. Please try again. ")
            
#Define the employee's home address
def obtain_employee_address():
    while True:
        try:
            #Obtain the employee's home address
            employee_address = input("Please enter the employee's home address(optional): ")
            #Declare the forbidden characters for the employee's home address
            forbidden_characters_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', '\\']
            #Validate that the employee's home address is correct
            if employee_address:
                if any(character in forbidden_characters_address for character in employee_address):
                    #If the employee's home address is incorrect, provide an error message and prompt the user to enter their home address again
                    print("Employee address was not formatted correctly. Please try again. ")
                else:
                    #If the employee's home address is correct, return the employee's home address
                    return employee_address
        except:
            print("Employee address was not formatted correctly. Please try again. ")
    
#set increment count variable to 0
Count = 0   
    
#Declare the employee dictionary limit
while Count < 5:
    #Call the obtain_employee_ID function
    employee_ID = obtain_employee_ID()
    #Call the obtain_employee_name function
    employee_name = obtain_employee_name()
    #Call the obtain_employee_email function
    employee_email = obtain_employee_email()
    #Call the obtain_employee_address function
    employee_address = obtain_employee_address()
    
    #Append employee data to the dictionary
    #If the employee's home address field was left blank or invalid, the if statement will be executed
    #If the employee's home address field was not left blank, the else statement will be executed
    
    if len(employee_address) == 0:
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
        Count += 1
        continue

#Print the dictionary
print("Here are the employee(s) that you entered into the database: ")
print(employee_data)