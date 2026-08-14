# Finalproject_Attendance-Tracker
## Overview

The Attendance Tracker is a Python-based application developed to record, manage, and process student attendance for individual class sessions.

The application allows users to register students, record attendance, view attendance records, calculate attendance percentages, and save attendance information in CSV format.

This project demonstrates the practical application of Python programming concepts, Pandas for data processing, date and time handling, functions, data structures, and input validation.

## Objectives

The main objectives of this project are to:

* Develop a simple system for recording student attendance.
* Automatically record the date and time of each attendance entry.
* Process attendance records using Pandas.
* Calculate the attendance percentage of each student.
* Generate attendance summaries showing attendance statistics.
* Store attendance records in a CSV file for further use.

## Features

* Student registration using a unique student ID.
* Viewing of registered students.
* Recording of attendance for individual class sessions.
* Attendance status selection as Present or Absent.
* Automatic recording of date and time.
* Displaying complete attendance records.
* Calculation of attendance percentages.
* Generation of attendance summaries.
* Exporting attendance records to a CSV file.
* Basic input validation and error handling.

## Attendance Percentage Calculation

The attendance percentage is calculated using the following formula:

```text id="k2k5j7"
Attendance Percentage = (Number of Classes Attended / Total Number of Classes) × 100
```

For example, if a student attends 8 out of 10 classes:

```text id="j7a3rc"
(8 / 10) × 100 = 80%
```

## Functions

The application is divided into several functions, with each function responsible for a specific operation:

```text id="7k3m1z"
add_student()
view_students()
select_student()
select_status()
get_date_time()
record_attendance()
create_dataframe()
view_attendance()
calculate_attendance()
save_attendance()
display_menu()
main()
```

## Technologies Used
* **Python** – Core programming language.
* **Pandas** – Used for organizing, processing, and analysing attendance data.
* **datetime** – Used to obtain and record the current date and time.
* **CSV** – Used for storing attendance records.
* **Functions** – Used to divide the program into manageable and reusable sections.
* **Dictionaries and Lists** – Used to store student and attendance information.
* **Loops and Conditional Statements** – Used to control program flow.
* **Exception Handling** – Used to handle invalid user input.
# Finalproject_Attendance-Tracker
