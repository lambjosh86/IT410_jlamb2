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
        new_salary = employee_salaries[count] * .05
        company_raises.append(new_salary)
    elif (employee_salaries[count] >= 24) and (employee_salaries[count] <= 26):
        new_salary = employee_salaries[count] * .04
        company_raises.append(new_salary)
    elif (employee_salaries[count] >= 26) and (employee_salaries[count] <= 28):
        new_salary = employee_salaries[count] * .03
        company_raises.append(new_salary)
    else:
        new_salary = employee_salaries[count] * .02
        company_raises.append(new_salary)
        
#step 7 - Complex condition example
# If the maximum hourly rate is greater than $37.30 and the number of underpaid salaries is greater than 0,
# or the number of employee numbers is greater than 100 and the sum of employee salaries is less than $5,000,
# then print a message indicating a potential budget issue.

if (max_hourly_rate > 37.30 and len(underpaid_salaries) > 0) or (len(employee_numbers) > 100 and sum(employee_salaries) < 5000):
    print("Potential budget issue: Check salary distribution and underpaid employees.")