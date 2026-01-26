# =========================================================
# 1) Calculator for two numbers
# =========================================================

# Take input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate results
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

# Check division by zero
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Cannot divide by zero"

# Display results
print("\n--- Calculator Results ---")
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
print("Division:", division_result)


# =========================================================
# 2) Total salary calculator
# =========================================================

# Take input from user
basic_salary = float(input("\nEnter basic salary: "))
bonus = float(input("Enter bonus amount: "))

# Calculate total salary
total_salary = basic_salary + bonus

# Display result
print("\n--- Total Salary ---")
print("Total salary is:", total_salary)


# =========================================================
# 3) Marks total and average
# =========================================================

# Take input from user
marks1 = float(input("\nEnter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

# Calculate total and average
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

# Display results
print("\n--- Marks Summary ---")
print("Total marks:", total_marks)
print("Average marks:", average_marks)


# =========================================================
# 4) Rectangle area and perimeter
# =========================================================

# Take input from user
length = float(input("\nEnter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display results
print("\n--- Rectangle Details ---")
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)


# =========================================================
# 5) Celsius to Fahrenheit converter
# =========================================================

# Take input from user
celsius = float(input("\nEnter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print("\n--- Temperature Conversion ---")
print(f"Temperature in Fahrenheit: {fahrenheit}")
