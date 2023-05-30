
#Create an empty list to store the employee's information
employee_data = []

#Set increment count variable to 0
Count = 0

while Count < 5:
    #Define control variable for the employee ID check loop
    validate_employee_ID_2 = False
    while validate_employee_ID_2 == False:
        try:
            #Obtain employee ID from user
            employee_ID = input("Please enter your employee ID: ")
            #Validate that the employee ID is correct
            validate_employee_ID = employee_ID.isdigit()
            if len(employee_ID) > 7 or validate_employee_ID == False:
                validate_employee_ID_2 == False
            else:
                break
        except:
            print("Employee ID was not formatted correctly. Please try again.")

    #Define control variable for the employee name check loop
    validate_employee_name_2 = True
 
    #Obtain the employee's name
    employee_name = input("Please enter your first name: ")
    #Declare the forbidden characters for the employee's name
    forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
                        
    while validate_employee_name_2:
        if employee_name:
            
            for character in employee_name:
                    if character in forbidden_characters_name:
                        validate_employee_name_2 = True
                        break #Stop the loop if a forbidden character is found, otherwise the loop will continue to run if the next character is valid
            else: #If no entry has been made
                validate_employee_name_2 = False
                
            if validate_employee_name_2:
                employee_name = print("Employee name was not formatted correctly. Please try again. ")
    
    #Obtain the employee's email address
    employee_email = input("Please enter your email address: ")
    Validate_Employee_Email = False
    
    #Declare the forbidden characters for the employee's email address
    forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
    
    ##To detect if there is an error, delcare a while not loop
    while not Validate_Employee_Email:
        if employee_email:
            
            #Declare for loop to confirm if forbidden characters are in the employee email address
            for character in employee_email:
                if character in forbidden_characters_email:
                    Validate_Employee_Email = False
                    break
                else:
                    Validate_Employee_Email = True
    
            #If the employee's email address field contains any forbidden characters or anything besides letters, reprompt the user, otherwise break the loop
            if not Validate_Employee_Email:
                employee_email = input("Employee email was not formatted correctly. Please try again. ")
    
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
            #If the employee's home address contains any forbidden characters, reprompt the user, otherwise break the loop
            if forbidden_characters_found == True:
                validate_employee_address_2 == False
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