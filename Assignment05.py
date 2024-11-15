# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Maddie, 11/11/24, created script
#             Maddie, 11/12/24, made some changes but haven't implemented .json use
#             Maddie, 11/13/24, final touches... or maybe not?
# ------------------------------------------------------------------------------------------ #
from io import TextIOWrapper
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course
    2. Show current data
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''
file: TextIOWrapper = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
parts: list[str] = []
# file: TextIOWrapper
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    #print(students)
    for row in file.readlines():
        # Transform the data from the file
        parts = row.strip().split(',')
        #print(student_data)
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]
        student_data = {'first':parts[0], 'last':parts[1], 'course':parts[2]}
        # Load it into our collection (list of lists)
        students.append(student_data)
        #print(students)
    file.close()
    print('student data:')
    print(student_data)
except FileNotFoundError:
    print('File not found. Creating...')
    open(FILE_NAME, "w")
except Exception as e:
    print('Unknown exception. Resetting roster')
    students = []
    print('Unknown exception',type(e),e,sep='\n')
finally:
    if file and not file.closed:
        file.close()
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First name must be alphabetic.')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('First name must be alphabetic.')
            course_name = input("Please enter the name of the course: ")
            student_data = {'first':student_first_name,'last':student_last_name,'course':course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first']} {student['last']} is enrolled in {student['course']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
           # raise Exception()
            file = open(FILE_NAME, "w")
            for student in students:
                json_data = f"{student['first']},{student['last']},{student['course']}"
                json.dump(json_data, file)

            print("The following data was saved to file:")
            for student in students:
                print(f"Student {student['first']} {student['last']} is enrolled in {student['course']}")
        except Exception as e:
            print('Error saving to file')
            print(e)
        finally:
            if file and not file.closed:
                file.close()

        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended. Goodbye")

'''[
  {"first": "Maddie","last": "Schiffler","course": "Python100"},
  {"first": "Taylor","last": "Swift","course": "Poetry100"}
]'''