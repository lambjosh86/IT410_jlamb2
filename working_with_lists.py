#step 1 - List of all courses taken at walsh college
courses = ["principles of business communication", "principles of management", "statistical methods for business", "business communication methods", "systems analysis and design", "networks and operating systems", "professonal communication", "server virtualization and performance engineering", "database design and development (sql)", "fundamentals of cyber security", "digital and network forensics", "security operations and awareness", "principles of software engineering", "cryptography"]

#step 2 - sort the list and print each course with specific message
courses.sort()

for course in courses:
    print("I have taken " + course.upper() + "at Walsh College.")
    
#step 3 - add upcoming courses to the list, resort the list, and print the list with a message
courses.append("advanced programming")
courses.append("ethical hacking strategies and tools")
courses.sort()

print("\nThis is my course of study with upcoming courses added:")
for course in courses:
     print(course.upper())
     
#step - 4 remove the courses that have been taken already
print("\nI do not have to take these courses:")
for course in courses[1:5]:
    print(course.upper())
for course in courses[6:16]:
    print(course.upper())
courses.remove("principles of business communication")
courses.remove("principles of management")
courses.remove("statistical methods for business")
courses.remove("business communication methods")
courses.remove("systems analysis and design")
courses.remove("networks and operating systems")
courses.remove("professonal communication")
courses.remove("server virtualization and performance engineering")
courses.remove("database design and development (sql)")
courses.remove("fundamentals of cyber security")
courses.remove("digital and network forensics")
courses.remove("security operations and awareness")
courses.remove("principles of software engineering")
courses.remove("cryptography")

#step 5 - print the remaining courses
print("\nI plan to take the following courses next term")
for course in courses:
    print(course.upper())

#step 6 - create a list of numbers 1-1000 that are divisible by 6
divisible_by_six = []
for number in range (6,1001,6):
    divisible_by_six.append(number)

#step 7 - print a list of the first 20 numbers divisible by 6
print("\nHere are twenty numbers divisible by 6.")
for number in range (0,20):
    print(divisible_by_six[number])
    
#step 8 - calculate the maximum number of the original large list
maximum_number = max(divisible_by_six)

#step 9 - print the maximum value in the list
print("\nThe maximum value in the list is:", maximum_number)

#step 10 - calculate the sum of values of the original large list between the 10th and 50th values
sum_values = sum(divisible_by_six[10:51])
print("\nHere is the sum of several values in the list:", sum_values)

#step 11 - overwrite the variable with the original large list
courses = divisible_by_six
 