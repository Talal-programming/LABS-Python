# =========================================
# Lab - Exception Handling, OOP, OS, Files
# =========================================

import os
import shutil

# =========================================
# Part 1 - Exception Handling (Division)
# =========================================
print("=== Division Program ===")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
else:
    print("Result:", result)


# =========================================
# Part 2 - Class Person
# =========================================
print("\n=== Person Class ===")

class Person:
    def __init__(self, name, age):
        self.name = name          # Public
        self.__age = age          # Private

    def update_age(self, new_age):
        self.__age = new_age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.__age)

person = Person("Talal", 22)
person.update_age(23)
person.display()


# =========================================
# Part 3 - Inheritance (Employee & Manager)
# =========================================
print("\n=== Inheritance Example ===")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def add_bonus(self, bonus):
        self.salary += bonus

    def display_info(self):
        print("Name:", self.name)
        print("Total Salary:", self.salary)

manager = Manager("Talal", 5000)
manager.add_bonus(1000)
manager.display_info()


# =========================================
# Part 4 - Student Class with Try/Except
# =========================================
print("\n=== Student Class ===")

class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        try:
            age = int(input("Enter student age: "))
            if age < 0:
                raise ValueError
            self.age = age
        except:
            print("Invalid age entered.")
            self.age = None

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student()
student.display()


# =========================================
# Part A - Working with Folders
# =========================================
print("\n=== Working with Folders ===")

base_folder = "lab_data"

if not os.path.exists(base_folder):
    os.mkdir(base_folder)

subfolders = ["input", "output", "logs"]

for folder in subfolders:
    path = os.path.join(base_folder, folder)
    if not os.path.exists(path):
        os.mkdir(path)

print("\nContents of lab_data:")
for item in os.listdir(base_folder):
    path = os.path.join(base_folder, item)
    if os.path.isdir(path):
        print(item, "- Directory")
    else:
        print(item, "- File")

# Rename logs to history
logs_path = os.path.join(base_folder, "logs")
history_path = os.path.join(base_folder, "history")

if os.path.exists(logs_path):
    os.rename(logs_path, history_path)


# =========================================
# Part B - Working with Text Files
# =========================================
print("\n=== Working with Text Files ===")

input_path = os.path.join(base_folder, "input", "notes.txt")
output_path = os.path.join(base_folder, "output", "summary.txt")

# Write 5 lines
with open(input_path, "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.write("Line 4\n")
    file.write("Line 5\n")

# Read file
with open(input_path, "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))

# Copy content
with open(output_path, "w") as file:
    file.writelines(lines)


# =========================================
# Part C - Using pyfiglet
# =========================================
print("\n=== Using pyfiglet ===")

try:
    import pyfiglet
    ascii_art = pyfiglet.figlet_format("Talal")
    figlet_path = os.path.join(base_folder, "output", "ascii.txt")

    with open(figlet_path, "w") as file:
        file.write(ascii_art)

    print("ASCII art saved successfully.")

except ImportError:
    print("pyfiglet is not installed. Install using: pip install pyfiglet")


# =========================================
# Part D - Cleanup Task
# =========================================
print("\n=== Cleanup ===")

lab4_data = "lab4_data"
history_folder = os.path.join(lab4_data, "history")

if os.path.exists(history_folder) and os.path.isdir(history_folder):
    try:
        os.rmdir(history_folder)
        print("Empty history folder deleted.")
    except:
        print("History folder is not empty or cannot be deleted.")
