🎭 Real-Life Story – "Wedding Invitation 📜"

Imagine you are getting married! 💍 Your wedding invitation list is finalized.
📌 You CANNOT modify the guest list after printing the invitation.
🔥 This is exactly how tuples work in Python!

You can create a tuple (invite guests ✅)

You cannot change it after creation (list is fixed ❌)

You can access and use it (see the list ✅)


📌 In short:
🔹 List = Editable Guest List (Mutable)
🔹 Tuple = Printed Wedding Card (Immutable)


✅ Tuple Basics – Creation & Accessing Elements

🎯 How to Create a Tuple?

guests = ("Raj", "Priya", "Anand", "Divya")
print(guests)
# Output: ('Raj', 'Priya', 'Anand', 'Divya')

🔥 Tuple is created using () (parentheses).


🎯 Accessing Elements

print(guests[1])  
# Output: Priya

🔥 Uses indexing like lists (0-based index).


🎯 Negative Indexing
print(guests[-1])  
# Output: Divya


🔥 Negative indexing works too! (-1 refers to the last element).


🎯 Slicing Tuples
print(guests[1:3])  
# Output: ('Priya', 'Anand')

🔥 Extracts a portion of the tuple.


✅ Tuple Operations – Combining & Multiplying
🎯 Concatenation (+)
📌 Use case: Merging guest lists


family = ("Mom", "Dad")
friends = ("Raj", "Priya")
guests = family + friends
print(guests)  
# Output: ('Mom', 'Dad', 'Raj', 'Priya')

🔥 Joins two tuples.


🎯 Repetition (*)
📌 Use case: If you need multiple wedding cards

print(family * 3)  
# Output: ('Mom', 'Dad', 'Mom', 'Dad', 'Mom', 'Dad')


🔥 Repeats the tuple multiple times.


✅ Tuple Methods – A to Z!
Method	Description
count()	Count occurrences of an item
index()	Find the index of an item
len()	Get the length of a tuple
min()	Get the smallest value
max()	Get the largest value
sum()	Get the sum of elements
sorted()	Sort a tuple (returns a list)
tuple()	Convert an iterable to a tuple
any()	Returns True if at least one element is True
all()	Returns True if all elements are True
zip()	Combine two tuples element-wise
enumerate()	Get index-value pairs


🎯 Counting & Finding Items
✅ count()
📌 Use case: Count how many times a guest is invited


guests = ("Raj", "Priya", "Anand", "Raj")
print(guests.count("Raj"))  
# Output: 2
🔥 Counts occurrences of an item.


✅ index()

📌 Use case: Find where a guest is in the list

print(guests.index("Priya"))  
# Output: 1
🔥 Returns the first occurrence index.



🎯 Finding Length, Min, Max, and Sum
✅ len()
📌 Use case: Get the number of guests

print(len(guests))  
# Output: 4
🔥 Returns the length of a tuple.



✅ min(), max(), sum()
📌 Use case: Works with numbers

ages = (25, 30, 18, 35)
print(min(ages))  # Output: 18
print(max(ages))  # Output: 35
print(sum(ages))  # Output: 108
🔥 Finds smallest, largest, and sum of values.



🎯 Sorting & Converting Tuples
✅ sorted()
📌 Use case: Sort tuple values


ages = (30, 18, 25, 35)
print(sorted(ages))  
# Output: [18, 25, 30, 35]
🔥 Returns a sorted list (not a tuple!).


✅ tuple()
📌 Use case: Convert a list into a tuple

names_list = ["Raj", "Priya", "Anand"]
names_tuple = tuple(names_list)
print(names_tuple)  
# Output: ('Raj', 'Priya', 'Anand')
🔥 Creates a tuple from any iterable.


🎯 Checking Conditions in Tuples
✅ any()
📌 Use case: Check if any value is True

values = (0, 0, 1, 0)
print(any(values))  
# Output: True

🔥 Returns True if at least one element is True.

✅ all()
📌 Use case: Check if all values are True

values = (1, 1, 1, 1)
print(all(values))  
# Output: True


🔥 Returns True if all elements are True.


🎯 Advanced Tuple Functions
✅ zip()
📌 Use case: Combine multiple tuples

names = ("Raj", "Priya", "Anand")
ages = (25, 30, 35)
combined = tuple(zip(names, ages))
print(combined)  
# Output: (('Raj', 25), ('Priya', 30), ('Anand', 35))


✅ enumerate()
📌 Use case: Get index and value

guests = ("Raj", "Priya", "Anand")
for index, name in enumerate(guests):
    print(index, name)
# Output:
# 0 Raj
# 1 Priya
# 2 Anand
🔥 Adds index to each element.

🎤 Interview Questions
1️⃣ What is the difference between a list and a tuple?
✅ List = Mutable, Tuple = Immutable

2️⃣ Why are tuples faster than lists?
✅ Since tuples are immutable, Python optimizes their storage

3️⃣ How to convert a tuple into a list?
✅ list(my_tuple)

4️⃣ Can you modify a tuple after creation?
❌ No, tuples are immutable!

🚀 Now you are a Tuple Master! 🚀🔥