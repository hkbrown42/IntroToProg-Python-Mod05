# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log:
#   Hannah Brown, 5/17/2025, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the data constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the data variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str = ""  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Please make sure the file you are trying to open actually exists!\n")
    print(type(e))
except Exception as e:
    print("There was a non-specific error!\n")
    print(type(e))
finally:
    if file.closed == False:
        file.close()

# Present and process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do?: ")

    # Input user data
    if menu_choice == "1":
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha() and student_first_name != "":
                    print("The first name cannot contain numbers.")
                    continue
                if student_first_name == "":
                    print("This field cannot be blank.")
                    continue
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha() and student_last_name != "":
                    print("The last name cannot contain numbers.")
                    continue
                if student_last_name == "":
                    print("This field cannot be blank.")
                    continue
                course_name = input("Please enter the name of the course: ")
                if course_name == "":
                    print("This field cannot be blank.")
                    continue
                student_data = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                students.append(student_data)
                print(f"You have registered {student_first_name} "
                      f"{student_last_name} for {course_name}.")
                break
            except Exception as e:
                print("There was a non-specific error!\n")
                print(type(e))

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} "
                  f"is enrolled in {student["CourseName"]}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file, indent=2)
            file.close()
            print("-" * 50)
            print("Here are the current student registrations: ")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} " 
                      f"is enrolled in {student["CourseName"]}")
            print("-" * 50)
            continue
        except TypeError as e:
            print("Please make sure the data is a valid JSON format!\n")
            print(type(e))
        except Exception as e:
            print("There was a non-specific error!\n")
            print(type(e))
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4.")

print("Program Ended.")
