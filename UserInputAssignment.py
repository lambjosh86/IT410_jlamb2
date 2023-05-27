while True:
    #Step 1 - Obtain employee ID from user
    employee_ID = input("Please enter your employee ID: ")

    #Step 2 - Validate that the employee ID is a number that is 7 or less digits long
    validate_employee_ID = employee_ID.isdigit()
    if len(employee_ID) > 7 or validate_employee_ID == False: 
        break

    #Step 3 - Obtain the employee's name
    employee_name = input("Please enter your first name: ")

    #Step 4 - Validate that the employee's name contains only letters from A-Z
    validate_employee_name = employee_name.isalpha()

    #Step 5 - Declare the forbidden characters for the employee's name
    forbidden_characters_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']

    #Step 6 - Test the employee's name for any forbidden characters using a for loop
    forbidden_characters_found = False
    for character in forbidden_characters_name:
        if character in employee_name:
            forbidden_characters_found = True
    
    #Step 7 - If the employee's name contains any forbidden characters, break the loop
    if forbidden_characters_found == True or validate_employee_name == False:
        break
    
    #Step 8 - Obtain the employee's email address
    employee_email = input("Please enter your email address: ")
    
    #Step 9 - Validate that the employee's email address is composed of primarily alphanumeric characters
    validate_employee_email = employee_email.isalnum()
    
    #Step 10 - Declare the forbidden characters for the employee's email address
    forbidden_characters_email = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}','\\']
    
    #Step 11 - Test the employee's email address to see if the field was left blank and if it contains any forbidden characters using a for loop
    #Check if the field was left blank 
    if len(employee_email) == 0:
        break
    #Test the employee's email address for any forbidden characters using a for loop
    forbidden_characters_found = False
    for character in forbidden_characters_email:
        if character in employee_email:
            forbidden_characters_found = True
    
    #Step 12 - If the employee's email address field was left blank and/or contains any forbidden characters, break the loop
    if forbidden_characters_found == True or validate_employee_email == False:
        break
    
    #Step 13 - Obtain the employee's home address
    employee_address = input("Please enter the employee's home address(optional): ")
    
    #Step 14 - Declare the forbidden characters for the employee's home address
    forbidden_characters_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', '\\']
    
    #Step 15 - Test the employee's home address for any forbidden characters using a for loop
    forbidden_characters_found = False
    for character in forbidden_characters_address:
        if character in employee_address:
            forbidden_characters_found = True
    
    #Step 16 - If the employee's home address contains any forbidden characters, break the loop
    if forbidden_characters_found == True:
        break
    
    #Step 17 - Print the employee's information
    #If the employee's home address field was left blank, print the employee's information without the home address using an if statement
    #If the employee's home address field was not left blank, print the employee's information with the home address using an else statement
    
    if len(employee_address) == 0:
        print(f"Hello, {employee_name}. Your Employee ID is {employee_ID}, and your email address is {employee_email}. You did not provide an address.")
    else:
        print(f"Hello, {employee_name}. Your Employee ID is {employee_ID}, and your email address is {employee_email}. Your address is {employee_address}.")
        
    #Step 18 - Break the loop
    break
    
