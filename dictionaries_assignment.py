#Step 1 - Create a list of employee data
employee_data = [1121, "Jackie Grainger", 22.22,
1122, "Jignesh Thrakkar", 25.25,
1127, "Dion Green", 28.75, False,
24.32, 1132, "Jacob Gerber",
"Sarah Sanderson", 23.45, 1137, True,
"Brandon Heck", 1138, 25.84, True,
1152, "David Toma", 22.65,
23.75, 1157, "Charles King", False,
"Jackie Grainger", 1121, 22.22, False,
22.65, 1152, "David Toma"]

#Step 2 - Create three lists to store employee data
employee_numbers = []
employee_names = []
employee_salaries = []

#Step 3 - Sort the employee data into the three lists without duplicates
for item in employee_data:
    if item not in employee_numbers and type(item) == int:
        employee_numbers.append(item)
    elif item not in employee_names and type(item) == str:
        employee_names.append(item)
    elif item not in employee_salaries and type(item) == float:
        employee_salaries.append(item)
        
#Step 4 - Create list to store multiplied hourly rates
total_hourly_rate = []

#Step 4.1 - Multiply each hourly rate by 1.3 and store in total_hourly_rate list
for count in range(0,len(employee_salaries)):
    new_value = employee_salaries[count] * 1.3
    total_hourly_rate.append(new_value)
    
#Step 4.2 - Find the maximum value in the total_hourly_rate list
max_hourly_rate = max(total_hourly_rate)
    
#Step 4.3 - Check if the maximum hourly rate exceeds $37.30
if max_hourly_rate > 37.30:
    print(f"${max_hourly_rate} may be a budget concern concerning salary expenses.")
    
#Step 5 - Create a list to store underpaid salaries
underpaid_salaries = []

#Step 5.1 - Check if each salary is between $28.15 and $30.65 and store in underpaid_salaries list
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > 28.15 and total_hourly_rate[count] < 30.65:
        underpaid_salaries.append(total_hourly_rate[count])

#Step 6 - Create a list to store calculated raises
company_raises = []

#Step 6.1 - Calculate raises based on hourly rate ranges and store in company_raises list
for count in range(0,len(employee_salaries)):
    if (employee_salaries[count] >= 22) and (employee_salaries[count] <= 24):
        new_salary = employee_salaries[count] * 1.05
        company_raises.append(new_salary)
    elif (employee_salaries[count] >= 24) and (employee_salaries[count] <= 26):
        new_salary = employee_salaries[count] * 1.04
        company_raises.append(new_salary)
    elif (employee_salaries[count] >= 26) and (employee_salaries[count] <= 28):
        new_salary = employee_salaries[count] * 1.03
        company_raises.append(new_salary)
    else:
        new_salary = employee_salaries[count] * 1.02
        company_raises.append(new_salary)
        
#step 7 - Combine employee data into a list of dictionary items
employee_dictionary =  [{"employee number": employee_numbers[0], "employee name": employee_names[0], "employee salary": employee_salaries[0], "total hourly rate": total_hourly_rate[0], "company raises": company_raises[0]},
                        {"employee number": employee_numbers[1], "employee name": employee_names[1], "employee salary": employee_salaries[1], "total hourly rate": total_hourly_rate[1], "company raises": company_raises[1]},
                        {"employee number": employee_numbers[2], "employee name": employee_names[2], "employee salary": employee_salaries[2], "total hourly rate": total_hourly_rate[2], "company raises": company_raises[2]},
                        {"employee number": employee_numbers[3], "employee name": employee_names[3], "employee salary": employee_salaries[3], "total hourly rate": total_hourly_rate[3], "company raises": company_raises[3]},
                        {"employee number": employee_numbers[4], "employee name": employee_names[4], "employee salary": employee_salaries[4], "total hourly rate": total_hourly_rate[4], "company raises": company_raises[4]},
                        {"employee number": employee_numbers[5], "employee name": employee_names[5], "employee salary": employee_salaries[5], "total hourly rate": total_hourly_rate[5], "company raises": company_raises[5]},
                        {"employee number": employee_numbers[6], "employee name": employee_names[6], "employee salary": employee_salaries[6], "total hourly rate": total_hourly_rate[6], "company raises": company_raises[6]},
                        {"employee number": employee_numbers[7], "employee name": employee_names[7], "employee salary": employee_salaries[7], "total hourly rate": total_hourly_rate[7], "company raises": company_raises[7]}]

#step - 8 - Print out the final list of employee data using a for loop
print("Employee dictionary list:")
for employee in employee_dictionary:
    print(employee)