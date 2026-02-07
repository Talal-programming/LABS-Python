# =========================================
# Control Structures (Part 1)
# Using: if, if/else, if/elif/else, match
# =========================================

# -----------------------------
# 1) Password Check
# -----------------------------
password = input("Enter the password: ")

if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")


# -----------------------------
# 2) Age Category
# -----------------------------
age = int(input("\nEnter your age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teen")
elif 20 <= age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")


# -----------------------------
# 3) Positive Number & Range Check
# -----------------------------
number = int(input("\nEnter a number: "))

if number > 0:
    print("Positive")
else:
    print("Not Positive")

if 10 <= number <= 50:
    print("The number is between 10 and 50")
else:
    print("The number is NOT between 10 and 50")


# -----------------------------
# 4) Traffic Light using match
# -----------------------------
color = input("\nEnter a color (red, yellow, green): ").lower()

if color == "":
    print("Invalid input (empty)")
else:
    match color:
        case "red":
            print("Stop")
        case "yellow":
            print("Get Ready")
        case "green":
            print("Go")
        case _:
            print("Invalid color")


# -----------------------------
# 5) Calculator Menu
# -----------------------------
print("\nMenu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an option (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case "1":
        print("Result:", num1 + num2)
    case "2":
        print("Result:", num1 - num2)
    case "3":
        print("Result:", num1 * num2)
    case "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid option")


# -----------------------------
# 6) Student Result & Grade
# -----------------------------
score = int(input("\nEnter student score: "))

if score >= 50:
    print("Status: Passed")
else:
    print("Status: Failed")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
