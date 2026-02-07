# =========================================
# Control Structures (Part 2)
# Using: for, while, range, +=, break, continue
# =========================================

# -----------------------------
# 1) Sum of Even Positive Numbers
# -----------------------------
total = 0

print("Enter up to 10 numbers (0 to stop):")
for i in range(10):
    num = int(input(f"Number {i+1}: "))

    if num == 0:
        break

    if num < 0:
        continue

    if num % 2 == 0:
        total += num

print("Final sum of even positive numbers:", total)


# -----------------------------
# 2) Multiplication Table
# -----------------------------
number = int(input("\nEnter a number for multiplication table: "))

for i in range(1, 13):
    result = number * i

    if result % 3 == 0:
        continue

    if result > 50:
        break

    print(f"{number} x {i} = {result}")


# -----------------------------
# 3) Guess the Secret Number
# -----------------------------
import random

secret = random.randint(1, 20)
attempts = 0

print("\nGuess the secret number (1 to 20):")

while True:
    guess = int(input("Your guess: "))

    if guess < 1 or guess > 20:
        continue

    attempts += 1

    if guess == secret:
        print("Correct! You guessed the number.")
        print("Valid attempts:", attempts)
        break
    else:
        print("Wrong guess, try again.")


# -----------------------------
# 4) Count Numbers Divisible by 4
# -----------------------------
n = int(input("\nEnter a number n: "))
count = 0

for i in range(1, n + 1):

    if i > 50:
        break

    if i % 8 == 0:
        continue

    if i % 4 == 0:
        count += 1

print("Count of numbers divisible by 4:", count)


# -----------------------------
# 5) Number Triangle Pattern
# -----------------------------
print("\nTriangle Pattern:")

for i in range(1, 6):
    for j in range(1, i + 1):

        if j == 3:
            continue

        if i * j > 6:
            break

        print(j, end=" ")
    print()
