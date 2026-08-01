# Hospital Patient Record System

## Project Description

The Hospital Patient Record System is a console-based Python application developed using Object-Oriented Programming (OOP) concepts. It allows users to manage patient records efficiently by performing operations such as adding, searching, updating, deleting, and displaying patient information.

Patient data is stored in a CSV file so that records are preserved even after the program is closed.

---

## Features

- Add Patient
- Display All Patients
- Search Patient
- Update Patient
- Delete Patient
- Save Records to CSV
- Load Records from CSV
- Exception Handling

---

## OOP Concepts Used

### 1. Classes and Objects
- Person
- Patient
- Hospital

### 2. Encapsulation
- Private attribute `__disease`
- Getter and Setter methods

### 3. Inheritance
- Patient inherits from Person

### 4. Abstraction
- Person is an abstract class using the `abc` module.

### 5. File Handling
- Reads and writes patient data using CSV files.

### 6. Exception Handling
- Handles invalid user input.
- Handles file-related errors.

---

## Files

main.py

person.py

patient.py

hospital.py

patients.csv

README.md

---

## How to Run

Open a terminal in the project folder.

Run:

python main.py

Follow the menu displayed on the screen.

---

## Author

Anunay Kumar Sah