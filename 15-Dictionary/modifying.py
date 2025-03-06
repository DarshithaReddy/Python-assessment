# Creating a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
print("Initial Dictionary:", students)

# Adding values to the dictionary
students[106] = "Frank"
print("\nAfter Adding ID 106:", students)

# Updating values in the dictionary
students[102] = "Brian"
print("\nAfter Updating ID 102:", students)

# Accessing values in the dictionary
print("\nStudent with ID 103:", students[103])

# Creating a nested dictionary (Student ID with nested details)
nested_students = {
    101: {"Name": "Alice", "Age": 20, "Grade": "A"},
    102: {"Name": "Bob", "Age": 21, "Grade": "B"},
    103: {"Name": "Charlie", "Age": 22, "Grade": "A"}
}
print("\nNested Dictionary:", nested_students)

# Accessing values from the nested dictionary
print("\nDetails of Student 102:", nested_students[102])
print("Grade of Student 103:", nested_students[103]["Grade"])

# Printing the keys present in the dictionary
print("\nKeys in Dictionary:", students.keys())

# Deleting a value from the dictionary
del students[104]
print("\nAfter Deleting ID 104:", students)
