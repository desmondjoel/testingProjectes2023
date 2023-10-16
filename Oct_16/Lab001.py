# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F) based on
# the following grading scale:

# input- score - 89

#output - B

# A: 90-100

# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59
score = None
score = int(input("Enter the Score\n"))
print(score)

if score > 89:
    print("The Student grade is A")
elif score > 79 & score < 90:
    print("The Student grade is B")
elif score > 69 and score < 80:
    print("The Student grade is C")
elif score > 59 and score < 70:
    print("The Student grade is D")
else:
    print("The Student grade is F")
