# This is an Attendance Tracker program, records and processes students' attendance and calculates their attendance percentage
import pandas as pd
from datetime import datetime


# This block is where student information and attendance records are stored 
students = {}
attendance_records = []

# This function block adds a new student
def add_student():

    student_id = input("Enter student ID: ").strip().lower()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    student_name = input("Enter student name: ").strip()

    if student_name == "":
        print("Student name cannot be empty.")
        return

    students[student_id] = student_name

    print("Student added successfully.")


# This function block displays all registered students
def view_students():

    if len(students) == 0:
        print("No students have been registered.")
        return

    print("\nRegistered Students")

    for student_id, student_name in students.items():
        print(f"{student_id} - {student_name}")


# This function block selects a student
def select_student():

    if len(students) == 0:
        print("No students have been registered.")
        return None

    student_list = list(students.items())

    print("\nStudents")

    for number, student in enumerate(student_list, start=1):
        print(f"{number}. {student[1]} ({student[0]})")

    try:
        choice = int(input("Select student number: "))

        if choice < 1 or choice > len(student_list):
            print("Invalid student selection.")
            return None

        student_id = student_list[choice - 1][0]

        return student_id

    except ValueError:
        print("Please enter a valid number.")
        return None


# This function block selects the attendance status
def select_status():

    print("\nAttendance Status")
    print("1. Present")
    print("2. Absent")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        return "Present"

    elif choice == "2":
        return "Absent"

    else:
        print("Invalid attendance status.")
        return None


# This function block gets the current date and time
def get_date_time():

    current_time = datetime.now()

    date = current_time.strftime("%Y-%m-%d")
    time = current_time.strftime("%H:%M:%S")

    return date, time


# This functionblock records attendance
def record_attendance():

    if len(students) == 0:
        print("Please add students first.")
        return

    class_name = input("Enter class name: ").strip()

    if class_name == "":
        print("Class name cannot be empty.")
        return

    student_id = select_student()

    if student_id is None:
        return

    status = select_status()

    if status is None:
        return

    date, time = get_date_time()

    student_name = students[student_id]

    attendance_records.append({
        "Student ID": student_id,
        "Student Name": student_name,
        "Class": class_name,
        "Date": date,
        "Time": time,
        "Status": status
    })

    print(f"Attendance recorded for {student_name}.")


# This function block converts the attendance records into a Pandas DataFrame
def create_dataframe():

    if len(attendance_records) == 0:
        return None

    attendance_data = pd.DataFrame(attendance_records)

    return attendance_data


# This function block displays all attendance records
def view_attendance():

    attendance_data = create_dataframe()

    if attendance_data is None:
        print("No attendance records found.")
        return

    print("\nAttendance Records")
    print(attendance_data.to_string(index=False))


# This function block calculates attendance percentages
def calculate_attendance():

    attendance_data = create_dataframe()

    if attendance_data is None:
        print("No attendance records found.")
        return

    total_classes = attendance_data.groupby(
        ["Student ID", "Student Name"]
    ).size()

    present_classes = attendance_data[
        attendance_data["Status"] == "Present"
    ].groupby(
        ["Student ID", "Student Name"]
    ).size()

    present_classes = present_classes.reindex(
        total_classes.index,
        fill_value=0
    )

    attendance_percentage = (
        present_classes / total_classes
    ) * 100

    print("\nAttendance Summary")

    for student in total_classes.index:

        student_id = student[0]
        student_name = student[1]

        total = total_classes[student]
        present = present_classes[student]
        absent = total - present
        percentage = attendance_percentage[student]

        print(f"\nStudent ID: {student_id}")
        print(f"Student Name: {student_name}")
        print(f"Total Classes: {total}")
        print(f"Present: {present}")
        print(f"Absent: {absent}")
        print(f"Attendance Percentage: {percentage:.2f}%")


# This function block saves attendance records to a CSV file
def save_attendance():

    attendance_data = create_dataframe()

    if attendance_data is None:
        print("No attendance records to save.")
        return

    attendance_data.to_csv(
        "attendance_records.csv",
        index=False
    )

    print("Attendance records saved successfully.")


# This function block displays the main menu
def display_menu():

    print("\n==============================")
    print("       ATTENDANCE TRACKER")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Record Attendance")
    print("4. View Attendance")
    print("5. Attendance Summary")
    print("6. Save Attendance")
    print("7. Exit")
# This function block runs the whole program
def main():

    start = True

    while start:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            record_attendance()

        elif choice == "4":
            view_attendance()

        elif choice == "5":
            calculate_attendance()

        elif choice == "6":
            save_attendance()

        elif choice == "7":
            print("Thank you for using the Attendance Tracker.")
            start = False

        else:
            print("Invalid choice. Please select from 1 to 7.")


# This calls the funtion to start the program
main()