# =========================================
# Functions, Lambda, Math, Regex
# =========================================

import math
import re


# -----------------------------
# 1) Circle Area & Circumference
# -----------------------------
def circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter circle radius: "))

area = circle_area(radius)
circumference = (lambda r: 2 * math.pi * r)(radius)

print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))


# -----------------------------
# 2) Find Numbers in String
# -----------------------------
text = input("\nEnter a string with numbers: ")

numbers = re.findall(r"\d+", text)
numbers = list(map(int, numbers))

def sum_numbers(nums):
    return sum(nums)

total = sum_numbers(numbers)
double = (lambda x: x * 2)(total)

print("Numbers found:", numbers)
print("Sum:", total)
print("Doubled value:", double)


# -----------------------------
# 3) Squares & Math Operations
# -----------------------------
user_input = input("\nEnter numbers separated by commas: ")
nums = list(map(float, user_input.split(",")))

def square_list(numbers):
    return list(map(lambda x: x**2, numbers))

squares = square_list(nums)
max_square = max(squares)
sqrt_sum = math.sqrt(sum(squares))

print("Squares:", squares)
print("Maximum square:", max_square)
print("Square root of sum of squares:", sqrt_sum)


# -----------------------------
# 4) Password & Average Score
# -----------------------------
password = input("\nEnter a password: ")

has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"\d", password)

if has_upper and has_lower and has_digit:
    strength = "Strong"
else:
    strength = "Weak"

scores_input = input("Enter 5 scores separated by spaces: ")
scores = list(map(float, scores_input.split()))

def average(nums):
    return sum(nums) / len(nums)

avg = average(scores)
rounded_avg = math.ceil((lambda x: x)(avg))

print("Password strength:", strength)
print("Rounded average score:", rounded_avg)


# -----------------------------
# 5) Vowel Words & Statistics
# -----------------------------
paragraph = input("\nEnter a paragraph: ")

vowel_words = re.findall(r"\b[aeiouAEIOU]\w*", paragraph)

def count_vowels(text):
    return len(re.findall(r"[aeiouAEIOU]", text))

total_vowels = count_vowels(paragraph)

lengths = list(map(lambda word: len(word), vowel_words))

if lengths:
    avg_length = round(sum(lengths) / len(lengths), 2)
else:
    avg_length = 0

print("Words starting with vowels:", vowel_words)
print("Total vowels:", total_vowels)
print("Average vowel-word length:", avg_length)


# =========================================
# Recursion + Try/Except
# =========================================


# -----------------------------
# 1) Factorial
# -----------------------------
try:
    num = int(input("\nEnter a non-negative integer: "))
    if num < 0:
        raise ValueError

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    print("Factorial:", factorial(num))

except:
    print("Invalid input for factorial.")


# -----------------------------
# 2) Fibonacci
# -----------------------------
try:
    n = int(input("\nEnter number of Fibonacci terms: "))
    if n <= 0:
        raise ValueError

    def fibonacci(x):
        if x <= 1:
            return x
        return fibonacci(x-1) + fibonacci(x-2)

    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

except:
    print("Invalid input for Fibonacci.")


# -----------------------------
# 3) Power (Recursive)
# -----------------------------
try:
    base = float(input("\nEnter base: "))
    exponent = int(input("Enter exponent: "))

    def power(b, e):
        if e == 0:
            return 1
        return b * power(b, e - 1)

    print("Result:", power(base, exponent))

except:
    print("Invalid input for power function.")
