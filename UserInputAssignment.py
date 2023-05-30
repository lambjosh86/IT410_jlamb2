while True:
    #Obtain employee ID from user
    employee_ID = input("Please enter your employee ID: ")

    #Validate that the employee ID is a number that is 7 or less digits long
    validate_employee_ID = employee_ID.isdigit()
    if len(employee_ID) > 7 or validate_employee_ID == False: 
        break

    #Obtain the employee's name
    employee_name = input("Please enter your first name: ")

    #Declare the forbidden characters for the employee's name
    forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\','0','1','2','3','4','5','6','7','8','9']

    #Test the employee's name for any forbidden characters using a for loop
    if employee_name:
        for character in employee_name:
            if character in forbidden_characters_name:
                validate_employee_name = False
                break #Stop the loop if a forbidden character is found, otherwise it could continue to the else statement
            else:
                validate_employee_name = True
    else: #No user input
        validate_employee_name = False
    
    #If the employee's name contains any forbidden characters, break the loop
    if validate_employee_name == False:
        break
                
    #Obtain the employee's email address
    employee_email = input("Please enter your email address: ")
    
    #Declare the forbidden characters for the employee's email address
    forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
    
    #Test the employee's email address to see if the field was left blank and if it contains any forbidden characters using a for loop
    #Check if the field was left blank 
    if len(employee_email) == 0:
        break
    #Test the employee's email address for any forbidden characters using a for loop
    if employee_email:
        for character in employee_email:
            if character in forbidden_characters_email:
                validate_employee_email = False
                break #Stop the loop if a forbidden character is found, otherwise it could continue to the else statement
            else:
                validate_employee_email = True
    else: #No user input
        validate_employee_email = False
        
    #If the employee's email address field was left blank and/or contains any forbidden characters, break the loop
    if validate_employee_email == False:
        break
    
    #Obtain the employee's home address
    employee_address = input("Please enter the employee's home address(optional): ")
    
    #Declare the forbidden characters for the employee's home address
    forbidden_characters_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', '\\']
    
    #Test the employee's home address for any forbidden characters using a for loop
    forbidden_characters_found = False
    for character in forbidden_characters_address:
        if character in employee_address:
            forbidden_characters_found = True
    
    #If the employee's home address contains any forbidden characters, break the loop
    if forbidden_characters_found == True:
        break
    
    #Print the employee's information
    #If the employee's home address field was left blank, print the employee's information without the home address using an if statement
    #If the employee's home address field was not left blank, print the employee's information with the home address using an else statement
    
    if len(employee_address) == 0:
        print(f"Hello, {employee_name}. Your Employee ID is {employee_ID}, and your email address is {employee_email}. You did not provide an address.")
    else:
        print(f"Hello, {employee_name}. Your Employee ID is {employee_ID}, and your email address is {employee_email}. Your address is {employee_address}.")
        
    #Break the loop
    break