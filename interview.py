
📌 1. What is Python?

💡 Simple Explanation:
Python is a high-level, interpreted, dynamically typed programming language that is easy to read and write. It is widely used for web development, data science, automation, AI, and more.
🎯 Real-Life Story:
Imagine you are a chef 🧑‍🍳. You want to cook a delicious dish 🍲. If you have to write a complex recipe in a difficult language (like Assembly or C++), it will take more time. But Python is like a simple recipe book with easy steps that anyone can follow! 📝

📝 Example Code:


print("Hello, World!")  # Python makes printing simple!


📌 2. What are the key features of Python?

📌 2. What are the key features of Python?
💡 Simple Explanation:
Python is:
✅ Easy to learn – Simple syntax like English
✅ Interpreted – Runs code line by line (no compilation needed)
✅ Dynamically Typed – No need to declare variable types
✅ Cross-platform – Works on Windows, Mac, Linux
✅ Extensive Libraries – Thousands of built-in libraries
✅ Object-Oriented – Supports OOP concepts like classes and objects

🎯 Real-Life Story:
Think of Python as a Swiss Army knife 🛠️. It has different tools (libraries) for different tasks—just like a Swiss Army knife has a knife, screwdriver, scissors, and more! 🔪✂️

x = 10      # Integer
x = "Hello" # Now it's a string
print(x)    # Python allows changing types easily

📌 3. What are the applications of Python?
💡 Where is Python Used?
🚀 Web Development – Django, Flask
🤖 AI & Machine Learning – TensorFlow, Scikit-learn
📊 Data Science – Pandas, NumPy
🔍 Automation & Scripting – Automate boring tasks
🎮 Game Development – Pygame
📱 App Development – Kivy


🎯 Real-Life Example:
Imagine you are Iron Man (Tony Stark) 🦾. Python is JARVIS, your AI assistant! 🤖 Python powers AI, automation, and web applications just like JARVIS helps Tony!

📝 Example Code (Automation Example - Rename Files in a Folder)

import os

for index, file in enumerate(os.listdir("my_folder")):
    os.rename(f"my_folder/{file}", f"my_folder/file_{index}.txt")
👆 This code renames all files inside "my_folder".




📌 4. How is Python different from other programming languages?
💡 Comparison Table:

Feature	Python	C++	Java
Syntax	Simple	Complex	Medium
Speed	Slower	Faster	Faster
Compilation	No (Interpreted)	Yes	Yes
Memory Management	Automatic (Garbage Collection)	Manual	Automatic
Libraries	Large	Medium	Large
🎯 Real-Life Story:
    
🚗 Python = Automatic Car (Easy to use, but not the fastest)
🏍 C++ = Racing Bike (Super fast, but hard to control)
🚆 Java = Train (Faster than Python, but needs setup)

📝 Example Code (Python vs. C++ Syntax Comparison)
✅ Python:
    
print("Hello, World!")

✅ C++:
    
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!";
    return 0;
}

Python is shorter and cleaner! 🎉

📌 5. What is PEP 8, and why is it important?
💡 Simple Explanation:
PEP 8 is Python Enhancement Proposal 8 – It’s like a style guide that tells us how to write clean and readable Python code!

🎯 Real-Life Example:
Imagine you’re writing an essay 📝. If there’s no punctuation, it becomes hard to read. PEP 8 helps keep Python clean and readable like good grammar in English!

📝 Example (Bad vs. Good Code - PEP 8 Guidelines)
🚨 Bad Code (No PEP 8)
def add(a,b):return a+b


✅ Good Code (Follows PEP 8)

def add(a, b):
    return a + b

📌 Why? – Spaces after commas, indentation, and readability improved!





📌 6. What are Python’s built-in data types?
💡 Data Types in Python:
📌 Numeric – int, float, complex
📌 Sequence – list, tuple, range
📌 Text – str
📌 Set – set, frozenset
📌 Mapping – dict
📌 Boolean – bool (True, False)

🎯 Real-Life Story:
Think of Python data types as different types of storage containers in a kitchen!

Think of Python data types as different types of storage containers in a kitchen!

List – A basket (can hold multiple items)

Tuple – A sealed box (unchangeable)

Dictionary – A labeled spice rack (key-value pairs)

📝 Example Code:
    
num = 10        # int
pi = 3.14       # float
name = "Python" # str
fruits = ["apple", "banana"] # list
info = {"name": "John", "age": 30} # dict



📌 7. What is the difference between a dynamically typed and statically typed language?
💡 Simple Explanation:
✅ Dynamically Typed (Python): No need to declare variable types!
✅ Statically Typed (C, Java): Must declare variable types!


🎯 Real-Life Story:
Imagine buying a T-shirt 👕.

Dynamically Typed (Python) – You walk into a shop and buy any T-shirt without choosing size!

Statically Typed (C, Java) – You must specify size (M, L, XL) before buying!

📝 Example Code:
✅ Python (Dynamically Typed)

x = 10      # x is an int
x = "Hello" # Now x is a str

✅ Java (Statically Typed)

int x = 10;
x = "Hello"; // ❌ Error! Cannot change type


📌 8. How is Python an interpreted language?
💡 Simple Explanation:
Python runs line by line (interpreted), unlike compiled languages like C.

🎯 Real-Life Example:
Think of an interpreter as a translator 🗣️. If someone speaks a foreign language, an interpreter translates sentence by sentence. Python does the same—executes code line by line instead of compiling everything at once!


📌 9. What is indentation in Python, and why is it important?
💡 Simple Explanation:
Indentation (spaces/tabs at the start of a line) defines code blocks in Python.

🎯 Real-Life Example:
Think of writing an essay. If there are no paragraphs or spaces, it becomes unreadable. Python enforces indentation for better readability.


📝 Example Code:
if True:
    print("Indented properly!")  # Correct

🚨 Wrong (No Indentation - Error!)


if True:
print("This will give an error!")  # IndentationError



📌 1. What are mutable and immutable types in Python?
💡 Simple Explanation:

Mutable 📝 – Can be changed after creation (e.g., list, dictionary, set)

Immutable 🔒 – Cannot be changed after creation (e.g., tuple, string, int)

🎯 Real-Life Story:
Imagine you buy a notebook 📖 and a printed book 📚.

Notebook (Mutable) – You can write, erase, and modify pages.

Printed Book (Immutable) – Once printed, you cannot change the text!

📝 Example Code:
    
    
    
# Mutable example - List (Can be modified)
my_list = [1, 2, 3]
my_list.append(4)  # Adding a new element
print(my_list)  # Output: [1, 2, 3, 4]

# Immutable example - Tuple (Cannot be modified)
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ ERROR! Tuples are immutable


📌 2. What is the difference between a list and a tuple?
💡 Key Differences:

Feature	List ([])	Tuple (())
Mutability	Mutable (Can be changed)	Immutable (Cannot be changed)
Performance	Slower (because it allows modifications)	Faster (due to immutability)
Syntax	list = [1, 2, 3]	tuple = (1, 2, 3)
🎯 Real-Life Story:

List = A whiteboard 📝 where you can erase and rewrite.

Tuple = A stone tablet 🪨 with permanent writing.

# List (Mutable)
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # [10, 20, 30, 40]

# Tuple (Immutable)
my_tuple = (10, 20, 30)
my_tuple[0] = 100  # ❌ TypeError! Tuples cannot be changed


📌 3. What are sets in Python?
💡 Simple Explanation:
A set is an unordered collection of unique elements. It does not allow duplicates.

🎯 Real-Life Story:
Think of a party invitation list 🎉. Even if someone accidentally enters their name twice, the final list will have unique names only.

# Creating a set
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} (No duplicates!)

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}



📌 4. How do you create a dictionary in Python?
💡 Simple Explanation:
A dictionary (dict) stores key-value pairs, like a real-world dictionary where each word (key) has a meaning (value).

🎯 Real-Life Story:
Imagine your phone contacts 📞. Each name (key) is linked to a phone number (value).

# Creating a dictionary
student = {"name": "John", "age": 25, "city": "New York"}

# Accessing values
print(student["name"])  # Output: John

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'grade': 'A'}


📌 5. What is the difference between None and 0 in Python?
💡 Simple Explanation:

None – Represents nothing or absence of a value.

0 – A valid number with a defined meaning.

🎯 Real-Life Story:

None = An empty plate 🍽️ (No food at all)

0 = A plate with zero apples 🍏 (Food exists but count is 0)

📝 Example Code:
    
    
x = None
y = 0

print(x is None)  # True (x has no value)
print(y == 0)     # True (y has a value, but it's zero)


📌 6. What is type casting? How do you perform it in Python?
💡 Simple Explanation:
Type casting converts one data type into another.

🎯 Real-Life Story:
Think of melting ice 🧊 → water 💧 → steam ☁️. It's still H₂O, but in different forms!

📝 Example Code:

# Integer to string
num = 10
str_num = str(num)
print(type(str_num))  # Output: <class 'str'>

# String to integer
str_val = "100"
int_val = int(str_val)
print(type(int_val))  # Output: <class 'int'>


📌 7. How do you check the data type of a variable?
💡 Simple Explanation:
Use the type() function to check a variable's data type.

📝 Example Code:
    
x = 10
y = 3.14
z = "Python"

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>


📌 8. How to convert a string to an integer in Python?
💡 Simple Explanation:
Use int() function to convert a string to an integer.

🎯 Real-Life Story:
You get a movie ticket 🎟️ where the seat number is printed as text ("25"). You need to convert it to a number to process it in the system.


str_number = "123"
num = int(str_number)
print(num + 1)  # Output: 124


📌 9. How does Python handle memory management?
💡 Simple Explanation:
Python uses automatic memory management with:

Garbage Collection 🗑️ – Removes unused objects automatically.

Reference Counting 🔢 – Deletes objects when they are no longer used.

🎯 Real-Life Story:
Imagine your computer desktop 🖥️.

Reference Counting: Deletes files when you empty the recycle bin.

Garbage Collection: Automatically removes temporary files!


import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Shows reference count of x


📌 10. What are global and local variables?
💡 Simple Explanation:

Local Variable – Defined inside a function, accessible only within it.

Global Variable – Defined outside a function, accessible anywhere.

🎯 Real-Life Story:

Local Variable = A chef’s secret recipe 🧑‍🍳 (Used only inside the restaurant)

Global Variable = McDonald's recipe 🍔 (Used worldwide!)


x = "Global Variable"

def my_function():
    y = "Local Variable"
    print(y)  # Accessible here

print(x)  # Accessible anywhere
# print(y)  # ❌ Error! y is not accessible outside the function




📌 1. What are the different types of operators in Python?
💡 Python has 7 types of operators:

Operator Type	Example	Usage
Arithmetic	+, -, *, /, //, %, **	Math operations
Comparison	==, !=, >, <, >=, <=	Compare values
Logical	and, or, not	Boolean logic
Bitwise	&, `	, ^, ~, <<, >>`
Assignment	=, +=, -=, *=, /=	Assign values
Identity	is, is not	Compare object identity
Membership	in, not in	Check membership in lists, tuples, sets


📌 2. What is the difference between == and is in Python?
💡 Simple Explanation:

== (Equality Operator) → Compares values 🔍

is (Identity Operator) → Compares memory location 🧠


🎯 Real-Life Story:
Imagine two twins 👬:

They look the same (==), but they are two different people (is)!


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (Same values)
print(a is b)  # False (Different memory locations)
print(a is c)  # True (Same memory location)


📌 3. What is the difference between = and ==?
💡 Simple Explanation:

= (Assignment Operator) → Assigns values 🔄

== (Equality Operator) → Checks if values are equal 🔍


x = 10  # Assignment
print(x == 10)  # True (Equality check)


📌 4. How does Python handle division with / and //?
💡 Difference:

/ (True Division) → Always returns float

// (Floor Division) → Returns integer (removes decimal part)

🎯 Real-Life Story:

/ = Cutting a cake 🍰 into equal parts (Exact answer, even fractions)

// = Dividing chocolate 🍫 among kids (No fractions, only whole pieces)


print(10 / 3)   # Output: 3.3333333
print(10 // 3)  # Output: 3


📌 5. What is the modulus operator (%) used for?
💡 Simple Explanation:

💡 Simple Explanation:

Finds the remainder when dividing two numbers.

🎯 Real-Life Story:
You have 7 chocolates 🍫 and want to divide among 3 kids.
Each gets 2 chocolates, but 1 remains → That’s the modulus!


print(10 % 3)  # Output: 1 (Remainder of 10 ÷ 3)


📌 6. What is operator precedence?
💡 Simple Explanation:
Operator precedence decides which operation is performed first when multiple operators are used.

🎯 Real-Life Story:

BODMAS rule 🧮 – Brackets first, then division, then addition!

📝 Example Code:
print(10 + 2 * 3)  # Output: 16 (Multiplication first)
print((10 + 2) * 3)  # Output: 36 (Brackets first)

Precedence	Operators
1 (Highest)	(), **
2	*, /, //, %
3	+, -
4 (Lowest)	==, !=, and, or


📌 7. How do bitwise operators work in Python?
💡 Simple Explanation:
They perform operations at the binary (bit) level.

Operator	Name	Example
&	AND	5 & 3 = 1
`	`	OR
^	XOR	5 ^ 3 = 6
~	NOT	~5 = -6
<<	Left Shift	5 << 1 = 10
>>	Right Shift	5 >> 1 = 2

print(5 & 3)  # Output: 1 (AND)
print(5 | 3)  # Output: 7 (OR)
print(5 ^ 3)  # Output: 6 (XOR)
print(~5)  # Output: -6 (NOT)
print(5 << 1)  # Output: 10 (Left Shift)
print(5 >> 1)  # Output: 2 (Right Shift)


📌 8. How does the not operator work?
💡 Simple Explanation:

Reverses a Boolean value (True becomes False and vice versa).

📝 Example Code:

print(not True)  # Output: False
print(not False)  # Output: True
print(not (5 > 3))  # Output: False


📌 9. What is the difference between and and or operators?
💡 Simple Explanation:
💡 Simple Explanation:

Operator	Meaning	Example
and	Returns True only if both conditions are true	True and False → False
or	Returns True if at least one condition is true	True or False → True
📝 Example Code:

print(True and False)  # Output: False
print(True or False)  # Output: True
print((5 > 3) and (8 > 10))  # Output: False


📌 10. What is the ternary operator in Python?
💡 Simple Explanation:

The ternary operator is a one-line if-else statement.

🎯 Real-Life Story:

Normal if-else → You check weather 🌦️ and then decide umbrella ☔ or sunglasses 🕶️

Ternary Operator → You decide in one line!

📝 Example Code:

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult



📌 1. Conditional Statements na enna?
💡 Simple Explanation:

Decision-making ku Python la conditional statements use pandrom.

Oru condition true ah irundha, athukulla iruka code execute aagum.

🎯 Real-Life Example:
👉 Situation: Nee oru restaurant la iruka 🍽️.

Pocket la cash irundha → Biryani order pandra 🍛

Cash illa → Just water than kudikka mudiyum 💧


money = 500

if money > 300:
    print("Order Biryani 🍛")
else:
    print("Drink Water 💧")
✅ Output: Order Biryani 🍛



📌 2. if, elif, else epdi use panrathu?
💡 Simple Explanation:

if → First condition check pandrom ✅

elif → Previous condition fail aana next check pandrom ✅

else → Mothama condition fail aana ithu execute aagum ✅

🎯 Real-Life Example:
👉 Situation: Nee shopping mall la iruka 🛍️.

Salary ₹50,000+ irundha → iPhone vaangu 📱

Salary ₹20,000+ irundha → Samsung vaangu 📱

Ithu rendu illa na → Nokia 1100 vaangu 📞


salary = 30000

if salary > 50000:
    print("Buy iPhone 📱")
elif salary > 20000:
    print("Buy Samsung 📱")
else:
    print("Buy Nokia 1100 📞")


📌 3. if vs elif difference enna?
💡 Key Difference:

if → First condition than check aagum ✅

elif → if fail aana next condition check aagum ✅

Multiple elif statements irukalam, but only one if & one else

📝 Example:

num = 0

if num > 0:
    print("Positive Number 😊")
elif num < 0:
    print("Negative Number 😞")
else:
    print("Zero! 😶")

✅ Output: Zero! 😶


📌 4. else illa na enna aagum?
💡 Simple Explanation:

else kodukala na, condition true illa na edhume execute aagaathu

temp = 10

if temp > 20:
    print("It's Hot 🔥")

print("Program continues... 😎")


✅ Output: Program continues... 😎


📌 5. Empty if statement epdi write panrathu? (pass use pannu)
💡 Sometimes namakku if block la enna code podanum nu theriyathu
💡 Python empty if block ah allow pannaathu → pass use panna vendiyathu

📝 Example:

age = 25

if age > 18:
    pass  # Future implementation
else:
    print("You are a minor!")

✅ No Output, but no error!


📌 6. One-line if statement epdi write panrathu?
💡 Simple ah single line la if-else write panna mudiyum!

🎯 Real-Life Example:

Regular if-else: "If mazhai varum na, umbrella eduthuko, illa na poi vidu" ☔

One-liner: "Umbrella eduthuko if mazhai varum, illa na poi vidu"

rain = True
print("Take Umbrella ☔") if rain else print("Go without it 😎")

✅ Output: Take Umbrella ☔ (if rain = True)


📌 7. Nested if statements epdi use panrathu?
💡 Oru if statement kulla vera if statement use panna mudiyum!

🎯 Real-Life Example:
👉 Situation: Nee bank la iruka 💰

ATM card irundha

Balance irundha → Cash withdraw pannu 💵

Balance illa → "Insufficient balance"

ATM card illa → "No ATM card"


atm_card = True
balance = 500

if atm_card:
    if balance > 0:
        print("Withdraw Cash 💵")
    else:
        print("Insufficient Balance ❌")
else:
    print("No ATM Card 😔")

✅ Output: Withdraw Cash 💵



📌 8. if condition la and, or, not epdi use panrathu?
💡 Logical Operators la and, or, not use panna mudiyum

🎯 Real-Life Example:

and → Rendu conditionum true aaganum ✅

or → Oru condition true aagum pothum ✅

not → Condition ah opposite aakka mudiyum ✅

age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive a car 🚗")
else:
    print("You cannot drive 🚫")

✅ Output: You can drive a car 🚗


📌 9. Boolean values Python epdi handle panrathu?
💡 Python la True = 1, False = 0 nu treat pannum!

📝 Example:

print(True + True)  # Output: 2
print(False + True)  # Output: 1
print(True * 5)  # Output: 5


📌 10. Truthy & Falsy values enna?
💡 Python la konja values False nu treat aagum

🎯 Falsy Values:

None, 0, "", [], {}, False
📝 Example:

if 0:
    print("This will not run")
else:
    print("0 is Falsy 😞")  # ✅ This runs

✅ Output: 0 is Falsy 😞


🔥 Super Summary:
✅ if, elif, else → Decision-making
✅ Nested if → if inside if
✅ and, or, not → Logical operations
✅ Boolean values → True = 1, False = 0
✅ Truthy & Falsy values → Some values behave like False



📌 1. Loops na enna?
💡 Simple Explanation:

Oru task repeated ah execute panna loops use panrom.

Example: School bell kattum podhu 1st period, 2nd period... 8th period nu cycle pogum.

Python la loops use pannuna same code repeated ah execute panna mudiyum!


🎯 Real-Life Example:

Loop illa: "Naan 10 times ‘Good Morning’ sollanum" → 10 lines of code! 😭

Loop use panna: Just 1 line la solve pannidalam! 😎

📝 Python Code Example (Loop illa na 😭):

print("Good Morning! ☀️")
print("Good Morning! ☀️")
print("Good Morning! ☀️")
# Repeated 10 times! 😭

📝 Python Code Example (Loop use panna 😎):

for i in range(10):
    print("Good Morning! ☀️")
✅ Output:

Good Morning! ☀️ (10 times)


📌 2. for loop epdi work agum?
💡 For loop is used to iterate over a sequence like list, tuple, dictionary, string, etc.

🎯 Real-Life Example:

Exam Hall la Answer Paper distribute pandra

Every student ku oru paper kudukanum

students = ["Rahul", "Priya", "Anu", "Vikram"]

for student in students:
    print(f"Giving paper to {student} 📄")
Giving paper to Rahul 📄  
Giving paper to Priya 📄  
Giving paper to Anu 📄  
Giving paper to Vikram 📄  


📌 3. while loop epdi work agum?
💡 While loop → Condition True iruka varaikkum execute aagum.

🎯 Real-Life Example:

Tea kudika oru cup fill panna vendiyathu! ☕

while use pannina: Cup full aagala varaikkum tea kudika mudiyum!


tea = 0  # Cup empty
while tea < 5:
    print(f"Sipping tea... ☕ ({tea + 1}/5)")
    tea += 1
print("Tea over! 😭")

Sipping tea... ☕ (1/5)  
Sipping tea... ☕ (2/5)  
Sipping tea... ☕ (3/5)  
Sipping tea... ☕ (4/5)  
Sipping tea... ☕ (5/5)  
Tea over! 😭  

📌 4. Infinite Loop na enna? Epdi create pandrathu?
💡 Infinite loop → Condition never becomes False, so loop never stops!

🎯 Real-Life Example:

Fan switch on pannitu marandhu vittom na fan stop aagatha! 🔄

📝 Python Code Example (⚠️ Infinite Loop!):

while True:
    print("Fan is running... 🔄")
🚨 Warning: Stop this loop manually using CTRL + C in terminal!


📌 5. break statement epdi use pandrathu?
💡 Loop la break use panna, loop instant ah stop aagum!

🎯 Real-Life Example:

Bus stop la bus vandha udaneye stop waiting & board the bus! 🚌

📝 Python Code Example:

for i in range(1, 10):
    if i == 5:
        print("Bus arrived at Stop 5 🚌")
        break  # Stop the loop
    print(f"Waiting at Stop {i}... 🏠")

Waiting at Stop 1... 🏠  
Waiting at Stop 2... 🏠  
Waiting at Stop 3... 🏠  
Waiting at Stop 4... 🏠  
Bus arrived at Stop 5 🚌  


📌 6. continue statement epdi use pandrathu?
💡 continue use panna, current iteration skip aagum, but loop continue aagum!

🎯 Real-Life Example:

Train station la nee Chennai ku pora train ah mattum than edukka pora!

Vera city ku pogura trains skip panna vendiyathu 🚆 

cities = ["Mumbai", "Delhi", "Chennai", "Kolkata"]

for city in cities:
    if city != "Chennai":
        continue  # Skip other cities
    print(f"Boarding Train to {city} 🚆")

Boarding Train to Chennai 🚆  

📌 7. Epdi loop exit panna? (break & exit())
💡 Loop la exit panna break or exit() use panna mudiyum

📝 Example (exit() stops full program! ⚠️)

for i in range(5):
    if i == 3:
        print("Exiting program 🚪")
        exit()
    print(i)

0  
1  
2  
Exiting program 🚪  


📌 8. Loop la else clause epdi use panrathu?
💡 Loop complete ah run aaguna than else execute aagum.

🎯 Real-Life Example:

Lost mobile phone theditu iruka 📱

Found aana stop panna vendiyathu, illana "Lost phone" nu sollanum!


items = ["Wallet", "Keys", "Bag"]

for item in items:
    if item == "Phone":
        print("Found Phone! 📱")
        break
else:
    print("Lost Phone! 😭")


📌 9. Nested Loops na enna?
💡 Loop kulla vera loop use panna mudiyum!

🎯 Real-Life Example:

Classroom la students ku marks podanum 🎓

Each student ku multiple subjects irukum


students = ["Rahul", "Priya"]
subjects = ["Math", "Science"]

for student in students:
    for subject in subjects:
        print(f"{student} got marks in {subject} 📖")
Rahul got marks in Math 📖  
Rahul got marks in Science 📖  
Priya got marks in Math 📖  
Priya got marks in Science 📖  


📌 10. Dictionary la epdi loop panna?
💡 Dictionary la key-value pairs iterate panna .items() use panna vendiyathu

🎯 Real-Life Example:

Restaurant menu la items & price list check panna! 🍕

📝 Python Code Example:


menu = {"Pizza": 250, "Burger": 150, "Pasta": 200}

for item, price in menu.items():
    print(f"{item} costs ₹{price} 🍽️")
Pizza costs ₹250 🍽️  
Burger costs ₹150 🍽️  
Pasta costs ₹200 🍽️  

🔥 Super Summary:
✅ for loop → Sequence iterate panna
✅ while loop → Condition met aagum varaikkum
✅ break → Loop stop pannum
✅ continue → Skip current iteration
✅ Nested loops → Loop inside loop
✅ Dictionary loop → .items() use panna

💯 Next enna topic venum? 🚀


📌 1. Function na enna?
💡 Definition:

Function → Oru task repeatedly perform panna reusable block of code

Code waste aagatha → Function create panna re-use panna mudiyum!

🎯 Real-Life Example:

Restaurant la dosa order pannina 👨‍🍳

Cook oru thadava than batter prepare pannuvaar

Athu repeat panna vendam → Same batter la multiple dosa seiyalam!

Python la function create panna, athu multiple times use panna mudiyum!

📝 Python Code Example:

def make_dosa():  
    print("Making dosa... 🥞")
    print("Serving dosa... 🍽️")

# Function call
make_dosa()
make_dosa()
Making dosa... 🥞  
Serving dosa... 🍽️  
Making dosa... 🥞  
Serving dosa... 🍽️  



📌 2. Function epdi define pannurathu?
💡 Syntax:

def function_name():
    # Code block
    return something  # (Optional)
🎯 Real-Life Example:

Bank la ATM balance check pannurathu! 🏦

Function name → check_balance()

Return value → 5000


def check_balance():
    return 5000  # Balance amount

balance = check_balance()
print(f"Your bank balance is ₹{balance} 🏦")


✅ Output:

Your bank balance is ₹5000 🏦  



📌 3. Function vs Method enna difference?
💡 Function → Independent ah work agum (Example: print())
💡 Method → Oru object kooda serndhu work agum (Example: string.upper())

🎯 Real-Life Example:

Function: Coffee machine la "Make Coffee" button press panna → Coffee ready! ☕

Method: Mobile la .vibrate() function call panna → Mobile vibrate aagum! 📱

# Function
def greet():
    return "Hello! 👋"

# Method (inside a string object)
message = "hello".upper()  # Method used on 'hello' string
print(greet())  # Function call
print(message)  # Method call
Hello! 👋  
HELLO  



📌 4. Arguments vs Parameters enna?
💡 Parameters → Function define pannum pothu kudukkurathu
💡 Arguments → Function call pannum pothu pass pannurathu

🎯 Real-Life Example:

Function: Order Pizza 🍕

Parameter: (Pizza Type)

Argument: (Cheese Pizza)
def order_pizza(type):  # Parameter
    print(f"Ordering {type} pizza 🍕")

order_pizza("Cheese")  # Argument
order_pizza("Veggie")

Ordering Cheese pizza 🍕  
Ordering Veggie pizza 🍕  

📌 5. Default Arguments enna?
💡 Parameter ku default value kuduthaa, function call la argument pass panna vendam!

🎯 Real-Life Example:

Coffee shop la default ah "Sugar - Medium" kudupaanga ☕

Nee "Sugar - High" venumna, mention panna vendiyathu!
def make_coffee(sugar="Medium"):
    print(f"Making coffee with {sugar} sugar ☕")

make_coffee()  # Default value use pannum
make_coffee("High")  # Argument override pannum
Making coffee with Medium sugar ☕  
Making coffee with High sugar ☕  


📌 6. return vs print enna difference?
💡 print() → Output display pannum (visible only, use panna mudiyathu)
💡 return → Value return pannum (store panna & use panna mudiyum!)
 🎯 Real-Life Example:

Restaurant waiter:

print() → Menu paper la price display pannurathu!

return → Bill la actual price add pannurathu!
def add(a, b):
    return a + b  # Value return pannum

result = add(5, 10)
print(result)  # Print pannurathu
15  

📌 7. *args and **kwargs enna?
💡 *args → Multiple arguments pass panna
💡 **kwargs → Key-value pairs pass panna

📌 7. *args and **kwargs enna?
💡 *args → Multiple arguments pass panna
💡 **kwargs → Key-value pairs pass panna

🎯 Real-Life Example:

Pizza toppings 🍕

*args → "Cheese", "Olives", "Corn"

**kwargs → size="Medium", crust="Thin"

def order_pizza(*toppings, **details):
    print(f"Pizza with toppings: {toppings}")
    print(f"Details: {details}")

order_pizza("Cheese", "Olives", size="Medium", crust="Thin")
Pizza with toppings: ('Cheese', 'Olives')  
Details: {'size': 'Medium', 'crust': 'Thin'}  



📌 8. Function pass panna epdi?
💡 One function ah another function ku argument ah pass panna mudiyum!

🎯 Real-Life Example:

"Google Maps" la find_route() function ku bus_route() function pass panna
def greet(name):
    return f"Hello, {name}!"

def display_message(func, name):
    message = func(name)
    print(message)

display_message(greet, "Manickaraj")
Hello, Manickaraj!  


📌 9. Recursion na enna?
💡 Function itself ah call pannum!

🎯 Real-Life Example:

Russian Doll concept! (Doll kulla vera doll → Repeat) 🎎

📝 Python Code Example (Factorial Calculation)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 5! = 5 × 4 × 3 × 2 × 1
120  

📌 10. Lambda Function na enna?
💡 One-line la function define panna lambda use pannalam!

🎯 Real-Life Example:

Online calculator la "Double" button click panna, number ×2 aagum

📝 Python Code Example:
double = lambda x: x * 2
print(double(5))


📌 1. What is a List in Python?
💡 Definition:

List → Oru mutable (change panna mudiyum) ordered collection of items

Duplicate values allow pannum!

🎯 Real-Life Example:

Shopping list 🛒 → "Milk, Bread, Eggs" → Oru ordered list

📝 Python Code Example:


📌 2. How to Create a List?
💡 Square brackets [ ] use pannitu values separate panna!

🎯 Real-Life Example:

Friends list create panna 👬

📝 Python Code Example:

friends = ["Arun", "Bala", "Catherine"]
print(friends)


📌 3. What are List Comprehensions?
💡 Short & Efficient way to create lists!

🎯 Real-Life Example:

Odd numbers list create panna (Without loop)

📝 Python Code Example:

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(odd_numbers)

[1, 3, 5, 7, 9]

📌 4. How to Access Elements in a List?
💡 Indexing [ ] or Slicing [start:end] use pannalam!

🎯 Real-Life Example:

Netflix la 1st movie check panna

movies = ["Inception", "Interstellar", "Tenet"]
print(movies[0])  # First movie
print(movies[-1]) # Last movie


📌 5. How to Add Elements to a List?
💡 append() - Single item add panna
💡 extend() - Multiple items add panna
💡 insert() - Specific position la add panna

🎯 Real-Life Example:

New movie list la add panna 🎬

movies = ["Inception", "Interstellar"]
movies.append("Dunkirk")  # Add single item
movies.extend(["Tenet", "Oppenheimer"])  # Add multiple items
movies.insert(1, "Batman Begins")  # Insert at index 1
print(movies)


📌 6. How to Remove Elements from a List?
💡 remove() - Value use panna remove panna
💡 pop() - Index use panna remove panna
💡 del - Entire list or specific index delete panna

🎯 Real-Life Example:

Grocery list la unwanted items remove panna


groceries = ["Milk", "Eggs", "Bread"]
groceries.remove("Eggs")  # Remove by value
print(groceries)

item = groceries.pop(1)  # Remove by index
print(groceries, "| Removed:", item)

del groceries[0]  # Delete first item
print(groceries)
['Milk', 'Bread']  
['Milk'] | Removed: Bread  
[]  


📌 7. How to Sort a List in Python?
💡 sort() - Ascending or descending order la sort panna
💡 sorted() - New sorted list return pannum (original list change aagathu)

🎯 Real-Life Example:

Exam marks sorted panna

marks = [85, 72, 90, 60]
marks.sort()  # Ascending order
print(marks)

sorted_marks = sorted(marks, reverse=True)  # Descending order
print(sorted_marks)

📌 8. How to Reverse a List?
💡 reverse() - Reverse order la change panna
💡 [::-1] - One-line la reverse panna

🎯 Real-Life Example:

Train number list reverse panna 🚆


📌 9. What is a Tuple? How is it Different from a List?
💡 Tuple → Immutable (Change panna mudiyathu) ordered collection
💡 List → Mutable (Change panna mudiyum)

🎯 Real-Life Example:

Aadhaar card la name & DOB change panna mudiyathu → Tuple

Instagram bio change panna mudiyum → List

my_list = ["Apple", "Banana", "Cherry"]
my_tuple = ("Apple", "Banana", "Cherry")

# List mutable
my_list[0] = "Mango"

# Tuple immutable (error varum)
# my_tuple[0] = "Mango"  # TypeError


📌 10. How to Convert Tuple to List and Vice Versa?
💡 list() - Tuple to List convert
💡 tuple() - List to Tuple convert

🎯 Real-Life Example:

Shopping items frozen panna (Tuple) & modify panna (List)

# Tuple to List
tup = ("Milk", "Eggs", "Bread")
lst = list(tup)
lst.append("Butter")
print(lst)

# List to Tuple
new_tup = tuple(lst)
print(new_tup)




📌 1. What is a String in Python?
💡 Definition:

String → Characters oda collection (Text store panna use aagum)

Single (') or Double (") quotes use panni store panna mudiyum!

🎯 Real-Life Example:

Instagram bio 😎 → "Hello, I'm a Python Developer"

Netflix movie title 🎬 → "Interstellar"

bio = "Hello, I'm a Python Developer"
movie = 'Interstellar'
print(bio)
print(movie)

Hello, I'm a Python Developer  
Interstellar  


📌 2. How to Create a String?
💡 Single, Double, Triple quotes use panna mudiyum!

🎯 Real-Life Example:

WhatsApp status, bio, paragraph store panna

single_quote = 'Hello!'
double_quote = "Python is amazing!"
multi_line = """This is
a multi-line
string."""
print(single_quote)
print(double_quote)
print(multi_line)


📌 3. What is String Slicing?
💡 Part of the string extract panna [start:end] use panna!

🎯 Real-Life Example:

Netflix la movie name la first 5 letters mattum edukanum
movie = "Interstellar"
print(movie[0:5])  # First 5 letters
print(movie[:5])   # Same as above
print(movie[6:])   # From index 6 to end
print(movie[-3:])  # Last 3 letters


📌 4. How to Concatenate Strings?
💡 Two or more strings join panna + use panna

🎯 Real-Life Example:

Instagram la First Name + Last Name store panna

first_name = "Elon"
last_name = "Musk"
full_name = first_name + " " + last_name
print(full_name)

📌 5. How to Find the Length of a String?
💡 len() function use panna

🎯 Real-Life Example:

Password length check panna 🔐
password = "Secure@123"
print(len(password))  # Length of the string


📌 6. Difference Between find() & index()?
💡 Both search a substring, but:

find() - Not found na -1 return pannum

index() - Not found na error throw pannum

🎯 Real-Life Example:

YouTube video description la "Python" word iruka check panna

text = "Learn Python Programming"

print(text.find("Python"))  # Found at index 6
print(text.find("Java"))    # Not found → -1

print(text.index("Python")) # Found at index 6
# print(text.index("Java")) # Not found → Error!

📌 7. Convert a String to Uppercase & Lowercase?
💡 upper() - Uppercase convert
💡 lower() - Lowercase convert

🎯 Real-Life Example:

User input la name small letters la iruntha uppercase panna

name = "elon musk"
print(name.upper())  # Convert to uppercase

shouting = "HELLO WORLD!"
print(shouting.lower())  # Convert to lowercase


📌 8. What Does strip() Do?
💡 Extra spaces remove panna strip() use pannalam!

🎯 Real-Life Example:

User form la email enter pannum pothu space iruntha remove panna
email = "   user@example.com   "
clean_email = email.strip()
print(clean_email)


📌 9. How to Replace a Substring in a String?
💡 replace(old, new) use panna

🎯 Real-Life Example:

Website la "http" ah "https" ah replace panna
url = "http://example.com"
secure_url = url.replace("http", "https")
print(secure_url)


📌 10. Difference Between split() & join()?
💡 split() - String ah list ah split panna
💡 join() - List ah string ah join panna

🎯 Real-Life Example:

User Full Name la first name & last name separate panna (split)

CSV file data list ah store pannitu comma use panni join panna (join)

# Split Example
full_name = "Elon Musk"
name_parts = full_name.split()  # Split by space
print(name_parts)

# Join Example
words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # Join with space
print(sentence)


1️⃣ What is a Dictionary in Python?
💡 Definition:

Dictionary → Key-Value pair store panna use aagum!

Curly Braces {} la store aagum

Keys unique irukanum, values duplicate irukalam!


order = {
    "order_id": 1234,
    "customer": "Manickaraj",
    "status": "Shipped"
}

user = {"name": "Elon", "age": 52, "city": "Texas"}
2️⃣ How to Create a Dictionary?
💡 Curly Braces {} or dict() function use panna mudiyum

📝 Python Code Example:

# Method 1: Curly Braces
user = {"name": "Elon", "age": 52, "city": "Texas"}
print(user)

# Method 2: dict() Function
user2 = dict(name="Jeff", age=60, city="Seattle")
print(user2)

{'name': 'Elon', 'age': 52, 'city': 'Texas'}
{'name': 'Jeff', 'age': 60, 'city': 'Seattle'}

3️⃣ How to Access Dictionary Values?
💡 Key use panni value access panna mudiyum

🎯 Real-Life Example:

Instagram la username access panna
user = {"name": "Elon", "age": 52, "city": "Texas"}

# Access value using key
print(user["name"])  # Elon
print(user["age"])   # 52

4️⃣ How to Update a Dictionary?
💡 New key-value add panna or existing update panna

🎯 Real-Life Example:

User address update panna

📝 Python Code Example:
user = {"name": "Elon", "age": 52, "city": "Texas"}

# Update city
user["city"] = "California"

# Add new key
user["email"] = "elon@spacex.com"

print(user)
{'name': 'Elon', 'age': 52, 'city': 'California', 'email': 'elon@spacex.com'}


5️⃣ What is the get() Method in Dictionaries?
💡 Key missing na error varama None return pannum!

🎯 Real-Life Example:

Email key iruka check panna
user = {"name": "Elon", "age": 52, "city": "Texas"}

print(user.get("email"))  # None (No error)
print(user.get("name"))   # Elon


6️⃣ How to Merge Two Dictionaries?
💡 update() use panna or {**dict1, **dict2} syntax use panna

🎯 Real-Life Example:

User profile + Contact details merge panna
user = {"name": "Elon", "age": 52}
contact = {"email": "elon@spacex.com", "phone": "123456789"}

# Method 1: update()
user.update(contact)
print(user)

# Method 2: ** unpacking
merged = {**user, **contact}
print(merged)

7️⃣ Difference Between .keys(), .values(), and .items()?
💡 Dictionary elements extract panna 3 methods

🎯 Real-Life Example:

E-commerce product details fetch panna
product = {"name": "Laptop", "brand": "Dell", "price": 70000}

print(product.keys())   # dict_keys(['name', 'brand', 'price'])
print(product.values()) # dict_values(['Laptop', 'Dell', 70000])
print(product.items())  # dict_items([('name', 'Laptop'), ('brand', 'Dell'), ('price', 70000)])

dict_keys(['name', 'brand', 'price'])
dict_values(['Laptop', 'Dell', 70000])
dict_items([('name', 'Laptop'), ('brand', 'Dell'), ('price', 70000)])

🎯 📌 Set in Python
8️⃣ What is a Set in Python?
💡 Set → Unique values store panna use aagum (Duplicate values illai!)

Curly Braces {} la store aagum

Indexing illa, order unpredictable!
🎯 Real-Life Example:

Unique email IDs store panna

YouTube watch history la duplicate remove panna
emails = {"user1@gmail.com", "user2@gmail.com", "user1@gmail.com"}  # Duplicate removed
print(emails)  # {'user1@gmail.com', 'user2@gmail.com'}


9️⃣ Key Features of a Set
✅ Unique values only!
✅ Unordered (Indexing illa!)
✅ Mutable (Modify panna mudiyum)
✅ Duplicates automatically remove aagum!

🔟 How to Perform Set Operations?
🎯 Real-Life Example:

YouTube watch history & Liked videos comparison

Common students between two classes find panna

A = {"Python", "Java", "C++"}
B = {"JavaScript", "Python", "C#"}

# Union → All unique elements
print(A | B)  # {'Python', 'Java', 'C++', 'JavaScript', 'C#'}

# Intersection → Common elements
print(A & B)  # {'Python'}

# Difference → A la irunthu B remove panna
print(A - B)  # {'Java', 'C++'}


🏆 📌 Exception Handling in Python
1️⃣ What is an Exception in Python?
💡 Definition:

Exception na program la run time error (Execution time la error varum)

Program crash aagala handle panna try-except use pannuvom!

Example: Division by zero, invalid file access, etc.

🎯 Real-Life Example:

ATM la wrong PIN kudutha "Invalid PIN" nu message varum

Google Chrome crash aana “Recover Pages” nu varum

a = 10
b = 0
print(a / b)  # ZeroDivisionError: division by zero
ZeroDivisionError: division by zero


2️⃣ Difference Between Syntax Error and Exception
🔍 Aspect	📝 Syntax Error	🛠 Exception
Definition	Code correct ah illainu Python solvudhu	Execution time la error varum
When?	Compile time (Before running)	Runtime (While running)
Example	print(Hello) (Quotes miss)	10 / 0 (ZeroDivisionError)


3️⃣ How to Handle Exceptions in Python?
💡 Use try-except to handle errors and prevent crashes

🎯 Real-Life Example:

Google Forms la "Submit" press panna internet illa na error varathu → Retry button varum

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
You cannot divide by zero!

4️⃣ What is the Use of try, except, and finally Blocks?
💡 finally block always execute aagum (even exception varunaa kooda!)

🎯 Real-Life Example:

ATM la cash withdraw panna attempt pannalum, "Thank You" message varum

try:
    print(10 / 0)  # Exception varum
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Execution completed!")  # Always run
You cannot divide by zero!  
Execution completed!

5️⃣ How to Raise an Exception in Python?
💡 raise use panni namma custom error throw panna mudiyum!

🎯 Real-Life Example:

Amazon la 18+ age illana alcohol buy panna mudiyathu

📝 Python Code Example:
age = 16
if age < 18:
    raise ValueError("You must be 18+ to access this service!")
ValueError: You must be 18+ to access this service!


   
6️⃣ What is the assert Statement Used for?
💡 Condition true illana AssertionError varum

🎯 Real-Life Example:

Login password should be minimum 8 characters

📝 Python Code Example:   

password = "abc"
assert len(password) >= 8, "Password must be at least 8 characters!"
✅ Output (Error):

AssertionError: Password must be at least 8 characters!


7️⃣ Difference Between except Exception and except:
🔍 Aspect	📝 except Exception	🚨 except:
Handles?	Only exceptions	Handles everything (Even system exit)
Recommended?	✅ Yes (Safer)	❌ No (Can hide errors)

try:
    print(10 / 0)
except Exception as e:  # Safer
    print(f"Error: {e}")

try:
    print(10 / 0)
except:  # Dangerous (Catches everything)
    print("Some error occurred")
Error: division by zero
Some error occurred


8️⃣ Common Built-in Exceptions in Python
❌ Exception	📝 Description	🔥 Example
ZeroDivisionError	Division by zero	10 / 0
ValueError	Wrong input value	int("abc")
IndexError	List index out of range	arr[10]
KeyError	Dictionary key not found	dict["missing"]
TypeError	Wrong type operation	"hello" + 5
FileNotFoundError	File not found	open("missing.txt")


9️⃣ How to Create a Custom Exception?
💡 class use panni namma own exception create panna mudiyum!

🎯 Real-Life Example:

Bank la minimum balance maintain panna vendiyathu

class InsufficientBalanceError(Exception):
    pass

balance = 500
withdraw = 1000

if withdraw > balance:
    raise InsufficientBalanceError("Insufficient funds in your account!")
InsufficientBalanceError: Insufficient funds in your account!


🔟 Difference Between raise and throw
🔍 Aspect	🚀 raise (Python)	🚀 throw (Other languages)
Usage	Exception handle panna	C++, Java la use pannuvanga
Syntax	raise ValueError("Error")	throw new Exception("Error")
Python la?	✅ Yes, raise use panna	❌ throw illa


🏆 📌 Basic OOP Concepts in Python
1️⃣ What is Object-Oriented Programming (OOP)?

💡 Definition:

OOP na real-world objects mathiri code write panrathu

Real-world objects oda behavior & properties store panna classes use pannuvom

Encapsulation, Inheritance, Polymorphism, and Abstraction are the main concepts!

🎯 Real-Life Example:

Oru "Car" nu oru class iruku → Athuku color, speed nu properties iruku

Honda, BMW, Audi ellam car objects (instances) nu solluvom

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("BMW", "Red")  # Object Creation
car2 = Car("Audi", "Black")
✅ BMW and Audi are objects of the Car class.


2️⃣ What are the Four Main Principles of OOP?

 What are the Four Main Principles of OOP?
🏆 Principle	💡 Definition	🎯 Real-Life Example
Encapsulation	Data protection using private variables	ATM PIN protect pannurathu
Inheritance	Child class gets properties from parent class	Son inherits father’s height
Polymorphism	Same function different behaviors	Car la start() bike la start()
Abstraction	Hide implementation, show only necessary details	Google Maps (Backend logic teriyathu, just navigation)


3️⃣ What is a Class in Python?
💡 Definition:

Class na blueprint / template for creating objects

Class la multiple objects create panna mudiyum


3️⃣ What is a Class in Python?
💡 Definition:

Class na blueprint / template for creating objects

Class la multiple objects create panna mudiyum

🎯 Real-Life Example:

"MobilePhone" class create pannuna → Nokia, iPhone ellam objects


class MobilePhone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


4️⃣ What is an Object in Python?
💡 Definition:

Object na class la create panna instance

Class la define panna properties & methods ellam object la use panna mudiyum

🎯 Real-Life Example:

MobilePhone class la "iPhone" and "Samsung" nu rendu object create pannalam
phone1 = MobilePhone("iPhone", 100000)
phone2 = MobilePhone("Samsung", 50000)

✅ phone1 and phone2 are objects of MobilePhone class.


5️⃣ How Do You Create a Class in Python?
💡 Use class keyword

📝 Syntax:
    class ClassName:
    # Class Body
 Real-Life Example:

Oru "Student" class create pannalam
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
✅ Student class ready!


6️⃣ How Do You Create an Object in Python?
💡 Class la object create panna class name use panni call pannanum

object_name = ClassName(arguments)
🎯 Real-Life Example:

Student class use panni rendu object create pannalam

student1 = Student("Raj", 21)
student2 = Student("Priya", 22)
✅ student1 and student2 are objects of the Student class.


7️⃣ What is the Difference Between a Class and an Object?
🔍 Aspect	📌 Class	🔥 Object
Definition	Blueprint for objects	Instance of a class
Memory?	Doesn't take memory	Takes memory
Example	Car class	BMW, Audi are objects

 Real-Life Example:

"House Plan" → Class

"My House" → Object

8️⃣ What is self in Python?
💡 self object-ku specific attributes store panna use aagum

 Real-Life Example:

"Raj" student ku roll number different, "Priya" ku different


class Student:
    def __init__(self, name, age):
        self.name = name  # Self stores object-specific data
        self.age = age
✅ Every object has unique name and age.

9️⃣ What is the __init__ Method in Python?
💡 __init__ is the constructor, automatically execute aagum when object create pannrom

🎯 Real-Life Example:

ATM la card insert panna automatically balance check pannum → __init__ method!

class Laptop:
    def __init__(self, brand, price):
        print("Laptop object created!")  # Auto-execute
        self.brand = brand
        self.price = price

l1 = Laptop("Dell", 60000)  # Auto runs __init__
Laptop object created!


🔟 Why is self Used in Methods?
💡 self use panna class oda attributes and methods objects kitta attach aagum

🎯 Real-Life Example:

Bike ku own speed irukum, self.speed use panna athu store aagum
class Bike:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"Bike Brand: {self.brand}, Speed: {self.speed} km/h")

bike1 = Bike("Yamaha", 120)
bike1.show_details()
Bike Brand: Yamaha, Speed: 120 km/h



🔹 1️⃣ What is Encapsulation in Python?

💡 Definition:

Encapsulation na data hide pannurathu, direct access kudukaama, secure panna use pannuvom

Class oda variables (attributes) ah protect panna encapsulation use pannuvom

Users can access only allowed data using methods (functions inside class)

🎯 Real-Life Example:

ATM PIN – Neenga PIN ah type pannuna backend la process aagum, direct access panna mudiyathu!

Doctor ku patient data access panna allow pannuvanga, aana public la access panna mudiyathu!

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance  # Accessing private variable through method

account = BankAccount(5000)
print(account.get_balance())  # ✅ Allowed
print(account.__balance)      # ❌ Error - Direct access not allowed

5000
AttributeError: 'BankAccount' object has no attribute '__balance'
✅ Encapsulation hides __balance and only allows access through get_balance() method.


🔹 2️⃣ How Do You Achieve Encapsulation in Python?

💡 Encapsulation achieve panna:

Private variables (__variable) - Restrict direct access

Methods for controlled access (getters & setters)

Property Decorators (@property) - Secure access

🎯 Real-Life Example:

Mobile la "IMEI Number" (unique ID) irukum, but neenga direct access panna mudiyathu!

Only authorized engineers access panna mudiyum
class Mobile:
    def __init__(self, model, imei):
        self.model = model
        self.__imei = imei  # Private variable

    def get_imei(self):
        return f"IMEI Number: {self.__imei}"  # Getter method

mobile = Mobile("iPhone 15", "123456789012345")
print(mobile.model)      # ✅ Allowed
print(mobile.get_imei()) # ✅ Allowed
print(mobile.__imei)     # ❌ Error - Private variable

✅ __imei direct access panna mudiyathu, only get_imei() method la access panna mudiyum!

🔹 3️⃣ What Are Public, Private, and Protected Variables in Python?
🔍 Variable Type	📌 Syntax	🔥 Access Level
Public	self.name	✅ Anyone can access
Protected	self._name	✅ Only class & subclass can access
Private	self.__name	❌ Cannot be accessed directly
🎯 Real-Life Example:

Public: Name, Age (Neenga freely access panna mudiyum)

Protected: Bank balance (Only customer & bank staff can access)

Private: ATM PIN (Neenga direct access panna mudiyathu!)

class Person:
    def __init__(self, name, age, salary):
        self.name = name        # Public
        self._age = age         # Protected
        self.__salary = salary  # Private

person = Person("Raj", 25, 50000)

print(person.name)     # ✅ Public - Allowed
print(person._age)     # ✅ Protected - Allowed (But not recommended)
print(person.__salary) # ❌ Private - Error

✅ name access panna mudiyum, __salary direct access panna mudiyathu!

🔹 4️⃣ What is the Difference Between _var, __var, and __var__?

🔍 Syntax	📌 Usage	🔥 Example
_var	Protected variable	_balance
__var	Private variable	__pin
__var__	Special (Dunder) method	__init__, __str__

🎯 Real-Life Example:

_var → "Handle with care" (Protected) - Example: _age

__var → "Confidential" (Private) - Example: __password

var → "System reserved" (Dunder methods) - Example: __init__

🔹 5️⃣ How Do You Access Private Variables in Python?

💡 Private variables access panna, use:

Getter methods (get_ methods)

Python Name Mangling (_ClassName__variable)

🎯 Real-Life Example:

Bank ATM PIN (Backend la store pannirukum, neenga direct access panna mudiyathu, but app use pannuna view panna mudiyum)

class Bank:
    def __init__(self, pin):
        self.__pin = pin  # Private variable

    def get_pin(self):   # Getter method
    
        return self.__pin

account = Bank("9876")
print(account.get_pin())       # ✅ Allowed
print(account._Bank__pin)      # ✅ Name mangling method (Not recommended)
print(account.__pin)           # ❌ Error

✅ Best practice: Use get_pin() method instead of account._Bank__pin (Name mangling).

🔹 6️⃣ What is the Purpose of Getters and Setters in Python?
💡 Getter & Setter methods use panna:
✅ Data protection
✅ Validation before modifying data
✅ Controlled access to private attributes

🎯 Real-Life Example:

Salary update panna HR permission venum, direct change panna mudiyathu!

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):  # Getter
        return self.__salary

    def set_salary(self, new_salary):  # Setter
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

emp = Employee(50000)
print(emp.get_salary())  # ✅ 50000
emp.set_salary(60000)    # ✅ Updated
print(emp.get_salary())  # ✅ 60000
✅ Direct access illa, but setter method use pannuna update panna mudiyum.

🔹 7️⃣ What is @property in Python?
💡 @property decorator use panna getters & setters simpler aagum

🎯 Real-Life Example:

Mobile battery level direct access panna mudiyathu, app la check panna mudiyum

class Laptop:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

laptop = Laptop(50000)
print(laptop.price)  # ✅ Allowed
laptop.price = 60000 # ✅ Setter works
print(laptop.price)  # ✅ 60000
✅ @property use panna simpler syntax la getters & setters use panna mudiyum!



🔹 1️⃣ What is Inheritance in Python?
💡 Definition:

Inheritance na oru class la iruka properties & methods ah vera oru class la use panradhu.

Child class (subclass) parent class (superclass) oda properties ah inherit pannidum.

Code reusability increase aagum, duplicate code avoid panna mudiyum!

🎯 Real-Life Example:

Father oda properties & skills son ku inherit aagum.

Father → Programming Expert

Son → Inherits programming skills + own gaming skills

class Father:  # Parent Class
    def programming(self):
        print("Father knows Python programming.")

class Son(Father):  # Child Class (inherits from Father)
    def gaming(self):
        print("Son knows gaming.")

son = Son()
son.programming()  # ✅ Inherited method
son.gaming()       # ✅ Own method
Father knows Python programming.
Son knows gaming.
✅ Son class inherits programming() from Father, and it also has its own gaming() method!

🔹 2️⃣ What Are the Types of Inheritance in Python?
✅ Python supports 5 types of inheritance:
1️⃣ Single Inheritance
2️⃣ Multiple Inheritance
3️⃣ Multilevel Inheritance
4️⃣ Hierarchical Inheritance
5️⃣ Hybrid Inheritance


🔹 3️⃣ What is Single Inheritance?
💡 Definition:

Oru parent class irukum, oru child class irukum.

Child class will inherit properties from the parent class.

🎯 Real-Life Example:

Dad oda driving skill son ku transfer aagum.
class Dad:  # Parent Class
    def drive(self):
        print("Dad can drive a car.")

class Son(Dad):  # Child Class
    def bike(self):
        print("Son can ride a bike.")

son = Son()
son.drive()  # ✅ Inherited
son.bike()   # ✅ Own method
✅ Single inheritance → One parent, one child!

🔹 4️⃣ What is Multiple Inheritance?
💡 Definition:

Oru child class ku multiple parent classes irukum.

Child class multiple classes oda properties ah inherit pannidum.

🎯 Real-Life Example:

Dad - Business skills, Mom - Cooking skills → Son inherits both!

class Dad:
    def business(self):
        print("Dad is a businessman.")

class Mom:
    def cooking(self):
        print("Mom is a great cook.")

class Son(Dad, Mom):  # Multiple Inheritance
    def sports(self):
        print("Son loves sports.")

son = Son()
son.business()  # ✅ Inherited from Dad
son.cooking()   # ✅ Inherited from Mom
son.sports()    # ✅ Own method
✅ Multiple inheritance → One child, multiple parents!

🔹 5️⃣ What is Multilevel Inheritance?
💡 Definition:

Chain pattern la inheritance nadakkum (Grandparent → Parent → Child).

Oru class oru class ah inherit pannum, appuram atha vera class inherit pannum.

🎯 Real-Life Example:

Grandfather → Father → Son (Skills transfer aagum!)

class Grandfather:
    def farming(self):
        print("Grandfather knows farming.")

class Father(Grandfather):
    def programming(self):
        print("Father knows Python.")

class Son(Father):
    def gaming(self):
        print("Son knows gaming.")

son = Son()
son.farming()     # ✅ Inherited from Grandfather
son.programming() # ✅ Inherited from Father
son.gaming()      # ✅ Own method
✅ Multilevel inheritance → One after another inheritance!

🔹 6️⃣ What is Hierarchical Inheritance?

💡 Definition:

One parent class, multiple child classes inherit from it.

🎯 Real-Life Example:

Dad → Son & Daughter (Dad skills shared with both!)


class Dad:
    def drive(self):
        print("Dad can drive.")

class Son(Dad):  # Inherits from Dad
    def bike(self):
        print("Son can ride a bike.")

class Daughter(Dad):  # Inherits from Dad
    def cycle(self):
        print("Daughter can ride a cycle.")

son = Son()
daughter = Daughter()

son.drive()  # ✅ Inherited
son.bike()   # ✅ Own method

daughter.drive()  # ✅ Inherited
daughter.cycle()  # ✅ Own method

🔹 7️⃣ What is Hybrid Inheritance?
💡 Definition:

Combination of multiple inheritance types.

Single + Multiple + Multilevel + Hierarchical mixed!

🎯 Real-Life Example:

School system → Students inherit from multiple teachers & parents!

class School:
    def educate(self):
        print("School provides education.")

class Sports:
    def play(self):
        print("Sports teach discipline.")

class Student(School, Sports):  # Multiple Inheritance
    def study(self):
        print("Student studies well.")

class Topper(Student):  # Multilevel Inheritance
    def rank(self):
        print("Topper ranks first.")

topper = Topper()
topper.educate()  # ✅ Inherited from School
topper.play()     # ✅ Inherited from Sports
topper.study()    # ✅ Inherited from Student
topper.rank()     # ✅ Own method
✅ Hybrid inheritance → Different inheritance types combined!


🔹 8️⃣ What is Method Overriding in Python?
💡 Definition:

Child class la same function name & parameters irundha, athu parent class function ah override pannidum!

🎯 Real-Life Example:

Dad driving slow, Son driving fast! (Same skill, different execution!)
class Dad:
    def drive(self):
        print("Dad drives safely.")

class Son(Dad):
    def drive(self):  # Overriding parent method
        print("Son drives fast!")

son = Son()
son.drive()  # ✅ Son's method overrides Dad's method!
✅ Method overriding → Child class function replaces parent class function!


🔹 9️⃣ How Do You Use super() in Python?
💡 Definition:

super() use panna parent class method ah call panna mudiyum!
🎯 Real-Life Example:

Son wants to drive fast but still respects Dad’s safe driving method!
class Dad:
    def drive(self):
        print("Dad drives safely.")

class Son(Dad):
    def drive(self):
        super().drive()  # Calls parent class method
        print("Son drives fast!")

son = Son()
son.drive()
✅ super().drive() parent class method call pannum!

🔹 🔟 Can Constructors Be Inherited?
💡 Yes! Parent class constructor (__init__) child class ku inherit aagum!

📝 Python Code Example:
class Parent:
    def __init__(self):
        print("Parent Constructor!")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent constructor
        print("Child Constructor!")

child = Child()
✅ Parent constructor call aagum, then child constructor call aagum!













