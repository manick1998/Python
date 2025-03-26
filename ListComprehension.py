🔥 List Comprehensions – Spoon-Feeding Mode 🍽️
🧠 List Comprehension Na Enna?
List Comprehension na oru shortcut way to create lists in Python.
Normal for loop la list create panna lines of code jaasthi aagum.
List Comprehension use panna single line la smart ah create panna mudiyum.




🎭 Real-Life Story – "Tiffin Box Sorting 🍱"
💡 Situation:
Imagine school students kitta tiffin box collect panni,
only "idly" vaangura students list ready panna solranga. 😅

Traditional way la nee epdi panva?
1. Students kitta oru oru tiffin open panni check pannu
2. Idly iruntha list la add pannu
3. Full list prepare pannu

🔥 But nee smart student!
Instead of checking one by one, oru shortcut technique use panni single step la complete panra!
Athuthan List Comprehension!


📝 Normal Way (Without List Comprehension)
tiffin_boxes = ["idly", "dosa", "idly", "poori", "idly", "chapati"]

idly_boxes = []  # Empty list to store idly boxes

for box in tiffin_boxes:
    if box == "idly":  # Check if the box contains idly
        idly_boxes.append(box)  # Add to the new list

print(idly_boxes)  # Output: ['idly', 'idly', 'idly']



🎯 List Comprehension Syntax

new_list = [expression for item in iterable if condition]

🔹 expression → Modify / Use the item
🔹 for item in iterable → Loop through list
🔹 if condition → Only include items that satisfy condition


🎬 More Real-Time Examples
🎯 Example 1: Even Numbers List (Traditional vs List Comprehension)
🔹 Situation: Friends oda roll number list la even numbers mattum filter pannanum!

❌ Without List Comprehension:
    
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # Output: [2, 4, 6, 8, 10]



✅ With List Comprehension:
    
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


🔥 1 line la work aagiduchu! 😎


🎯 Example 2: Squares of Numbers
🔹 Situation: 1-10 numbers oda squares list venum!

✅ With List Comprehension:
    
squares = [num ** 2 for num in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

💡 Shortcut! For loop la iteration panna venam, directly list la store panniduchu!


🎯 Example 3: Uppercase Conversion
🔹 Situation: Employee names list iruku, uppercase la change panna solranga!

✅ With List Comprehension:
    
🔥 Smart Code! 🚀


🎤 Interview Questions
1️⃣ What is List Comprehension in Python?
🔹 Answer: List comprehension is a concise way to create lists in Python using a single line of code instead of a traditional loop.

2️⃣ What is the difference between List Comprehension & for loop?
🔹 Answer: List comprehension is faster & concise, whereas for loops take more lines & are slower.

3️⃣ Can we use multiple conditions inside List Comprehension?
🔹 Answer: Yes, we can use if and even multiple if-else conditions inside List Comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_even = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(odd_even)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


🔥 Final Summary
✅ List Comprehension = Shortcut for creating lists
✅ Syntax: [expression for item in iterable if condition]
✅ Faster, Cleaner, and More Pythonic
✅ Reduces multiple lines of code into a single line



💡 🔥 Hands-on Task for You! 🚀 Try writing a List Comprehension to:
1️⃣ Filter numbers divisible by 5 from a list [10, 23, 45, 60, 7, 9, 50]
2️⃣ Convert only first letter of each word to uppercase from ["hello", "world", "python"]
3️⃣ Generate a list of cubes for numbers 1-10

Post your answers, I'll check & guide you! 🎯🔥