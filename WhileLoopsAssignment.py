
#Create an empty list to store the employee's information
employee_data = []

#Set increment count variable to 0
Count = 0

while Count <= 5:
    #Define control variable for the employee ID check loop
    validate_employee_ID_2 = False
    while validate_employee_ID_2 == False:
        try:
            #Obtain employee ID from user
            employee_ID = input("Please enter your employee ID: ")

            #Validate that the employee ID is a number that is 7 or less digits long
            validate_employee_ID = employee_ID.isdigit()
            if len(employee_ID) > 7 or validate_employee_ID == False:
                validate_employee_ID_2 = False
            else:
                break
        except:
            print("Employee ID was not formatted correctly. Please try again. ")

    #Define control variable for the employee name check loop
    validate_employee_name_2 = False
    while validate_employee_name_2 == False:
        try:
            #Obtain the employee's name
            employee_name = input("Please enter your first name: ")

            #Validate that the employee's name contains only letters from A-Z
            validate_employee_name = employee_name.isalpha()

            #Declare the forbidden characters for the employee's name
            forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']

            #Test the employee's name for any forbidden characters using a for loop
            forbidden_characters_found = False
            for character in forbidden_characters_name:
                if character in employee_name:
                    forbidden_characters_found = True
            #If the employee's name contains any forbidden characters, break the loop
            if forbidden_characters_found == True or validate_employee_name == False:
                validate_employee_name_2 = False
            else:
                break
        except:
            print("Employee name was not formatted correctly. Please try again. ")
    
    #Define control variable for the employee email check loop
    validate_employee_email_2 = False
    
    #Declare the forbidden characters for the employee's email address
    forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
    
    while validate_employee_email_2 == False:
        try:
            #Obtain the employee's email address
            employee_email = input("Please enter your email address: ")
            
            #Test the employee's email address for any forbidden characters using a for loop
            forbidden_characters_found = False
            for character in forbidden_characters_email:
                if character in employee_email:
                    forbidden_characters_found = True
            
            #If the employee's email address field contains any forbidden characters or anything besides letters, reprompt the user, otherwise break the loop
            if (forbidden_characters_found == True) or (len(employee_email) == 0):
                validate_employee_email_2 = False
            else:
                break
        except:
            print("Employee email was not formatted correctly. Please try again. ")
    
    #Define control variable for the employee address check loop
    validate_employee_address_2 = False
    while validate_employee_address_2 == False:
        try:
            #Obtain the employee's home address
            employee_address = input("Please enter the employee's home address(optional): ")
            
            #Declare the forbidden characters for the employee's home address
            forbidden_characters_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', '\\']
    
            #Test the employee's home address for any forbidden characters using a for loop
            forbidden_characters_found = False
            for character in forbidden_characters_address:
                if character in employee_address:
                    forbidden_characters_found = True
                    break
                 
            #If the employee's home address contains any forbidden characters, reprompt the user, otherwise break the loop
            if forbidden_characters_found == True:
                validate_employee_address_2 = False
            else:
                break
        except:
            print("Employee address was not formatted correctly. Please try again. ")
            
    #Append employee data to the dictionary
    #If the employee's home address field was left blank or invalid, the if statement will be executed
    #If the employee's home address field was not left blank, the else statement will be executed
    
    if len(employee_address) == 0:
        employee_data.append({"Employee ID": employee_ID,"Name": employee_name.title(), "Email": employee_email})
    else:
        employee_data.append({"Employee ID": employee_ID,"Name": employee_name.title(), "Email": employee_email, "Home Address": employee_address})
        
    #Prompt the user if they would like to enter another employee's information
    #If the user types "N", the loop will break and, the program will print the dictionary
    #If the user types "Y", they will be prompted to enter another employee's information
    
    enter_another_employee = input("Would you like to enter another employee's information? (Y/N): ").lower()
    if enter_another_employee == "N":
        break
    elif enter_another_employee == "Y":
        Count += 1
        continue
    
    if len(employee_data) == 5:
        print("You have reached the maximum number of employees that can be entered."

#Print the dictionary
print("Here are the employee(s) that you entered into the database: ")
print(employee_data)