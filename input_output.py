🔥 Input and Output (I/O) – 
✅ What is Input and Output in Python?
📌 Input → User-kitta data eduthukardhu
📌 Output → Screen (Terminal) la data print pannardhu

Idhula 2 main functions use pannuvom:
🔹 input() – User kitta data edukkum
🔹 print() – Data terminal la show pannum




1️⃣ Taking Input from User – input()

variable = input("Message to user: ")
 Example:

name = input("Enter your name: ")
print("Hello, " + name + "!")



🚀 Real-Life Example – Coffee Shop Order
💡 Situation: Coffee shop la nee order panna pora. Cashier unna kettu input() edukkuraan.


coffee = input("What coffee do you want? ")
print("You ordered:", coffee)



👉 User cappuccino kuduthaa, output → "You ordered: cappuccino"



2️⃣ Reading Different Data Types from Input
🔹 By Default, input() String ah dha edukkum!
🔹 Integer Input Example

age = input("Enter your age: ")  # Default: String
age = int(age)  # Convert to int
print("Your age after 5 years:", age + 5)


👉 User 25 kudutha, output → "Your age after 5 years: 30"

🔹 Float Input Example
price = float(input("Enter price: "))
print("Price after discount:", price - 5.5)


👉 User 100 kudutha, output → "Price after discount: 94.5"

3️⃣ Printing Output – print()
🔹 Syntax:

print("Message")


Example

print("Hello, World!")


✅ Output: Hello, World!

4️⃣ Formatted Output – Using f-strings
🔹 Example:
    
    
    
name = "Manick"
age = 25
print(f"My name is {name} and I am {age} years old.")



✅ Output: My name is Manick and I am 25 years old.

🔥 Why use f-strings?

String concatenate panna + podama direct {} use pannalam
Code neat ah irukum



5️⃣ Printing Multiple Values
🔹 Comma (,) Use Pannalam

print("My name is", name, "and my age is", age)


🔹 Using sep (Separator)

print("Python", "Java", "C++", sep=" | ")
✅ Output: Python | Java | C++


🔹 Using end (No Newline)

print("Hello", end=" ")
print("World!")


✅ Output: Hello World! (Same line la print aagum)

🔥 3 Real-Time Use Cases
🏢 1. User Login System
💡 Scenario: Website user email & password enter panna sollanum.

email = input("Enter your email: ")
password = input("Enter your password: ")
print(f"Welcome, {email}!")


👉 User abc@gmail.com kuduthaa, output → "Welcome, abc@gmail.com!"

🏦 2. ATM Withdrawal System
💡 Scenario: ATM la balance check panna user kitta amount input edukkanum.


balance = 5000  # Initial balance
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print(f"Transaction successful! Remaining balance: {balance}")
else:
    print("Insufficient funds!")


👉 User 2000 kuduthaa, output → "Transaction successful! Remaining balance: 3000"



📊 3. Shopping Cart Bill Calculation
💡 Scenario: User 2 items price enter pannum, total bill calculate pannum.

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))

total = item1 + item2
print(f"Total bill amount: ₹{total}")


🎯 Interview Questions & Answers
❓ 1. What is the default data type of input()?
✅ Answer: By default, input() string ah edukkum.

❓ 2. How to take integer input from user?
✅ Answer: Use int() function.

num = int(input("Enter a number: "))



❓ 3. What is the use of sep in print()?
✅ Answer: sep separator define pannum. Example:
    
    print("A", "B", "C", sep="-")  # Output: A-B-C


🚀 Summary
✅ input() – User kitta data edukkum
✅ print() – Data terminal la show pannum
✅ Formatted output – f-strings
✅ Real-world examples – Login system, ATM, Shopping Cart
✅ Interview preparation – Common questions & answers

🔥 Ippo Input & Output (I/O) concept 100% crystal clear! 😎🔥 Doubt irundha kelunga! 🚀
