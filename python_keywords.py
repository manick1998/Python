🔥 Python Keywords –

💡 Edhukku use pandrom?
Python keywords na predefined words. Intha words Python-kku special meaning irukum. Edhula oru keyword-a namma variable name-a use panna mudiyathu!

🔥 Example: if, else, for, while, return, class, try, except, break, continue, etc.
💡 Total: 35 keywords in Python (Python 3.10 version)


✅ Python Keywords List
🔥 All keywords (alphabetical order)

Category	Keywords
Control Flow	if, elif, else, for, while, break, continue, pass
Exception Handling	try, except, finally, raise, assert
Functions & Classes	def, return, lambda, class, yield
Data Handling	True, False, None, global, nonlocal
Logical Operators	and, or, not, is, in
Importing Modules	import, from, as
Object-Oriented	class, self
Memory Management	del
Multi-threading	async, await


🔥 Rules:
✅ Keywords case-sensitive (True correct, but true error!)
✅ Keywords variables ah use panna mudiyadhu (def = 10 ❌)


🚀 Story-Based Learning – Python Keywords
🏦 Real-Life Scenario 1: ATM Withdrawal – Keywords Usage
💡 Scenario:

Bank la oruthan withdraw panna poran
ATM Balance check pannum
Balance if withdrawal amount vitta adhigama iruntha, transaction continue aagum
If False, ATM raise panna "Insufficient Balance"


balance = 5000  
withdraw_amount = int(input("Enter withdrawal amount: "))

if withdraw_amount > balance:  
    raise Exception("Insufficient Balance")  
else:  
    balance -= withdraw_amount  
    print(f"Transaction Successful! Remaining balance: {balance}")  

💡 Used Keywords:
✅ if → Condition check
✅ raise → Error throw panna
✅ else → If false na default action



🎓 Real-Life Scenario 2: College Admission – Keywords Usage
💡 Scenario:

Student admission ku apply pannuran
80% vitta adhigama irundha admit panna vendiyadhu
Otherwise "Better luck next time" sollanum
If sports quota na, 70% vitta mela irundha admit panna vendiyadh

marks = int(input("Enter your percentage: "))  
sports_quota = input("Sports Quota? (yes/no): ").lower() == "yes"

if marks >= 80:  
    print("Admission Granted!")  
elif sports_quota and marks >= 70:  
    print("Admission Granted under Sports Quota!")  
else:  
    print("Better luck next time!")  


💡 Used Keywords:
✅ if → Admission check
✅ elif → Alternative condition
✅ else → Default case



🚦 Real-Life Scenario 3: Traffic Signal – Keywords Usage
💡 Scenario:

if red light na "STOP"
elif yellow light na "SLOW DOWN"
elif green light na "GO"
else → Invalid signal

signal = input("Enter Traffic Signal (red/yellow/green): ").lower()  

if signal == "red":  
    print("STOP!")  
elif signal == "yellow":  
    print("SLOW DOWN!")  
elif signal == "green":  
    print("GO!")  
else:  
    print("Invalid Signal!")  


💡 Used Keywords:
✅ if, elif, else


🚀 Python Keywords Explanation – Full Breakdown
🔹 1. Boolean Keywords: True, False, None
🔥 Example: Voting System


age = int(input("Enter your age: "))  
is_eligible = age >= 18  # `True` or `False` store aagum  

if is_eligible:  
    print("You can vote!")  
else:  
    print("You cannot vote!")  

✅ True → Condition satisfy panna
✅ False → Condition satisfy panna mattena
✅ None → No value store panna


🔹 2. Conditional Keywords: if, elif, else
🔥 Example: Mobile Discount Offer

price = int(input("Enter Mobile Price: "))

if price > 50000:  
    print("10% Discount!")  
elif price > 30000:  
    print("5% Discount!")  
else:  
    print("No Discount!")  

✅ Used For Decision Making


🔹 3. Looping Keywords: for, while, break, continue, pass
🔥 Example: Printing Numbers


for i in range(1, 6):  
    if i == 3:  
        continue  # 3 skip aagum  
    print(i)  

🔹 Output: 1 2 4 5 (3 skip aagum)
✅ for → Loop
✅ while → Condition based looping
✅ break → Loop stop panna
✅ continue → Next iteration ku poganum
✅ pass → Empty block maintain panna


🔹 4. Function Keywords: def, return
🔥 Example: Square of a Number

def square(num):  
    return num * num  

print(square(5))  # Output: 25  

✅ def → Function define panna
✅ return → Function value return panna


🔹 5. Exception Handling: try, except, finally, raise
🔥 Example: Division by Zero Handling

try:  
    num = int(input("Enter a number: "))  
    print(10 / num)  
except ZeroDivisionError:  
    print("Cannot divide by zero!")  
finally:  
    print("Program Ended!")  
✅ try → Error check panna
✅ except → Error handle panna
✅ finally → Always execute aagum
✅ raise → Custom error throw panna


🔹 6. Object-Oriented Keywords: class, self, __init__
🔥 Example: Car Class

class Car:  
    def __init__(self, brand):  
        self.brand = brand  

    def show(self):  
        print(f"Car Brand: {self.brand}")  

car1 = Car("Tesla")  
car1.show()  


✅ class → OOP create panna
✅ self → Object refer panna
✅ __init__ → Constructor define panna

🎯 Interview Questions & Answers
❓ 1. What are Python Keywords?
✅ Python la special reserved words, built-in functionalities provide pannum!

def = 10  # ❌ Syntax Error!


❓ 3. How to list all keywords in Python?
import keyword  
print(keyword.kwlist)  

👉 Output la 35 keywords list varum!

# 🚀 Conclusion
# ✅ Python la 35 keywords iruku
# ✅ Variables ah keywords use panna mudiyadhu
# ✅ Keywords are case-sensitive!
# ✅ If-else, loops, functions, OOP keywords ellame mukkiyam!









