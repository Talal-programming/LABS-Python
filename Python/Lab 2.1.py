# =========================================
# Lists, Tuples, Dictionaries, and Sets
# =========================================

# -----------------------------
# 1) List: Numbers Operations
# -----------------------------
numbers = []

print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

total_sum = sum(numbers)
average = total_sum / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("\nList Results:")
print("Numbers:", numbers)
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)


# -----------------------------
# 2) Tuple: Words Operations
# -----------------------------
words = []

print("\nEnter 5 words:")
for i in range(5):
    word = input(f"Word {i+1}: ")
    words.append(word)

words_tuple = tuple(words)

print("\nTuple Results:")
print("Words:", words_tuple)
print("First word:", words_tuple[0])
print("Last word:", words_tuple[-1])
print("Total words:", len(words_tuple))

search_word = input("Enter a word to search: ")
if search_word in words_tuple:
    print("The word is found in the tuple.")
else:
    print("The word is NOT found in the tuple.")


# -----------------------------
# 3) Dictionary: Students Scores
# -----------------------------
students = {}

print("\nEnter 3 students and their scores:")
for i in range(3):
    name = input("Student name: ")
    score = float(input("Score: "))
    students[name] = score

print("\nStudents and Scores:")
for name, score in students.items():
    print(name, ":", score)

highest_student = max(students, key=students.get)
print("Highest score:", highest_student, "with score", students[highest_student])


# -----------------------------
# 4) Sets: Union, Intersection, Difference
# -----------------------------
list1 = input("\nEnter numbers for first list (separated by space): ").split()
list2 = input("Enter numbers for second list (separated by space): ").split()

set1 = set(map(int, list1))
set2 = set(map(int, list2))

print("\nSet Results:")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))


# -----------------------------
# 5) Combined List, Tuple, Dictionary, Set
# -----------------------------
names = []

print("\nEnter 5 names:")
for i in range(5):
    name = input(f"Name {i+1}: ")
    names.append(name)

names_tuple = tuple(names)
print("\nNames Tuple:", names_tuple)

name_lengths = {}
for name in names:
    name_lengths[name] = len(name)

print("Dictionary (Name Lengths):", name_lengths)

lengths_set = set(name_lengths.values())
print("Set of Unique Name Lengths:", lengths_set)
