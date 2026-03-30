# Task 1 – Data Parsing & Profile Cleaning

# Explanation:
# 1. Cleaned names using strip() and title() to remove spaces and fix casing
# 2. Converted roll number from string to integer using int()
# 3. Converted marks_str into a list using split() and map()
# 4. Checked name validity using isalpha()
# 5. Printed formatted output using f-strings

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()
    
    # Convert roll to integer
    roll = int(student["roll"])
    
    # Convert marks_str to list of integers
    marks = list(map(int, student["marks_str"].split(", ")))
    
    # Validate name (only alphabets in each word)
    is_valid = all(word.isalpha() for word in name.split())
    
    # Store cleaned data
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    
    # Print validation result
    if is_valid:
        print(f"{name} → ✓ Valid name")
    else:
        print(f"{name} → ✗ Invalid name")
    
    # Print formatted profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

# Print name in ALL CAPS and lowercase for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nName transformations for roll 103:")
        print(student["name"].upper())
        print(student["name"].lower())
        
        # Task 2 – Marks Analysis Using Loops & Conditionals

# Explanation:
# 1. Used for loop with zip() to print subject, marks and assign grades
# 2. Calculated total, average, highest and lowest marks
# 3. Used while loop to add new subjects dynamically
# 4. Handled invalid inputs using try-except and range checking
# 5. Calculated updated average after adding new subjects

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"\nStudent: {student_name}\n")

# ----------- Part 1: Subject + Grade -----------
for sub, mark in zip(subjects, marks):
    if 90 <= mark <= 100:
        grade = "A+"
    elif 80 <= mark <= 89:
        grade = "A"
    elif 70 <= mark <= 79:
        grade = "B"
    elif 60 <= mark <= 69:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{sub} : {mark} → Grade {grade}")

# ----------- Part 2: Calculations -----------
total = sum(marks)
average = round(total / len(marks), 2)

# Highest and lowest
max_mark = max(marks)
min_mark = min(marks)

highest_subject = subjects[marks.index(max_mark)]
lowest_subject  = subjects[marks.index(min_mark)]

print("\n--- Summary ---")
print(f"Total Marks      : {total}")
print(f"Average Marks    : {average}")
print(f"Highest Scoring  : {highest_subject} ({max_mark})")
print(f"Lowest Scoring   : {lowest_subject} ({min_mark})")

# ----------- Part 3: While Loop (Marks Entry System) -----------
new_count = 0

print("\nEnter new subjects (type 'done' to stop):")

while True:
    sub = input("Enter subject name: ")
    
    if sub.lower() == "done":
        break
    
    mark_input = input("Enter marks (0–100): ")
    
    try:
        mark = int(mark_input)
        
        if 0 <= mark <= 100:
            subjects.append(sub)
            marks.append(mark)
            new_count += 1
            print("Added successfully!\n")
        else:
            print("⚠ Invalid marks! Must be between 0 and 100.\n")
    
    except ValueError:
        print("⚠ Invalid input! Please enter numeric marks.\n")

# ----------- Final Output -----------
updated_average = round(sum(marks) / len(marks), 2)

print("\n--- Updated Details ---")
print(f"New Subjects Added : {new_count}")
print(f"Updated Average    : {updated_average}")

# Task 3 – Class Performance Summary

# Explanation:
# 1. Used loop to calculate each student's average marks
# 2. Assigned Pass/Fail based on average ≥ 60
# 3. Printed formatted table using f-strings
# 4. Counted total pass and fail students
# 5. Found class topper and overall class average

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
topper_name = ""
topper_avg = 0
total_avg_sum = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg
    
    # Pass or Fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
    
    # Check topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    # Print formatted row
    print(f"{name:<18} | {avg:^7} | {status}")

# Class average
class_average = round(total_avg_sum / len(class_data), 2)

print("\n--- Summary ---")
print(f"Passed Students : {pass_count}")
print(f"Failed Students : {fail_count}")
print(f"Class Topper    : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_average}")

# Task 4 – String Manipulation Utility

# Explanation:
# 1. Used strip() to remove extra spaces
# 2. Converted text to title case using title()
# 3. Counted occurrences using count()
# 4. Replaced words using replace()
# 5. Split sentences using split()
# 6. Printed numbered sentences with formatting

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print("Step 1 – Clean Essay:")
print(clean_essay)

# Step 2: Title Case
print("\nStep 2 – Title Case:")
print(clean_essay.title())

# Step 3: Count 'python'
print("\nStep 3 – Count of 'python':")
count_python = clean_essay.count("python")
print(count_python)

# Step 4: Replace 'python' with 'Python 🐍'
print("\nStep 4 – Replace 'python':")
replaced_text = clean_essay.replace("python", "Python 🐍")
print(replaced_text)

# Step 5: Split into sentences
print("\nStep 5 – Sentences List:")
sentences = clean_essay.split(". ")
print(sentences)

# Step 6: Numbered sentences
print("\nStep 6 – Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    # Ensure sentence ends with '.'
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
    