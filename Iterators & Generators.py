🔥 Iterators & Generators

📌 1. What is an Iterator?
💡 Iterator na enna?
Iterator na oru item set (list, tuple, etc.) la irundhu oru item-a oru time-ku eduthu kudukkura system.
Think of it like a TV remote → Button press panna oru oru channel sequentially change aagum.


🎯 Real-Life Example 1 – Automatic Ticket Dispenser at Railway Station 🚉
🚊 Situation:

Train ticket vending machine la queue la nikiravanga automatic-a oru oru ticket receive pannuvanga.
Machine 1st person ku ticket kudukkum, then next person ku ticket varum.
Last person kitta reach aagum bodhu "No More Tickets Available" nu message varum.
🔹 This is exactly how an Iterator works!
✅ Sequentially item provide pannum
✅ End reach aagum bodhu StopIteration error throw pannum


📌 1. Iterator – What is it?
💡 Iterator na enna?
👉 Iterator na oru list, tuple, set la irukura items-a oru oru item-a eduthu kudukkum system.
👉 Think of it like YouTube Auto-Play → Next video next video nu sequential-a play aagum!

🎯 Real-Life Story – School Teacher & Attendance Register 👩‍🏫
Teacher oru oru student name register la paathu attendence poduva.
1st student name read pannuva → Present / Absent note pannuva
2nd student, 3rd student… ippadi sequential-a pogum
Last student varaikum attendence eduthuttu "No More Students Available!" nu solliduva
🔥 Ithu dhan Iterator concept!
✅ Sequential-a items provide pannum
✅ End reach aagum bodhu StopIteration error varum

class AttendanceRegister:
    def __init__(self, students):
        self.students = students
        self.index = 0  # Start from the first student

    def __iter__(self):
        return self  # Iterator instance return pannum

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration  # No more students
        student = self.students[self.index]
        self.index += 1
        return student

# Students list
students_list = ["Arun", "Bala", "Chitra", "Divya"]
attendance = AttendanceRegister(students_list)

# Oru oru student name print pannum
for student in attendance:
    print(f"📢 Calling: {student}")


📢 Calling: Arun
📢 Calling: Bala
📢 Calling: Chitra
📢 Calling: Divya



class TicketDispenser:
    def __init__(self, tickets):
        self.tickets = tickets
        self.index = 0

    def __iter__(self):
        return self  # Iterator instance return pannum

    def __next__(self):
        if self.index >= len(self.tickets):
            raise StopIteration  # No more tickets
        ticket = self.tickets[self.index]
        self.index += 1
        return ticket

ticket_machine = TicketDispenser(["🎫 Ticket 1", "🎫 Ticket 2", "🎫 Ticket 3"])
for ticket in ticket_machine:
    print(f"🛤️ Collect Your {ticket}")
    
    
    
🔥 2. Creating an Iterator in Python

numbers = [10, 20, 30, 40]  # List of numbers
my_iter = iter(numbers)  # Convert to iterator

print(next(my_iter))  # 🔥 1st item
print(next(my_iter))  # 🔥 2nd item
print(next(my_iter))  # 🔥 3rd item
print(next(my_iter))  # 🔥 4th item


10
20
30
40
⚠️ 5th time next(my_iter) call panna error varum (StopIteration Exception)!





📌 2. Generator – What is it?
💡 Generator na enna?
👉 Iterator ku advanced version!
👉 Generator yield use panni items-a one by one generate pannum (No need to store all data in memory!)
👉 Lazy evaluation → Demand iruntha than generate pannum!

🎯 Real-Life Story – Tea Shop & Unlimited Tea 🍵
Normal Hotel la: You order tea → They prepare & serve → Finish aagum
Tea Kada la (Generator! 🤩):
✅ Tea master always hot tea ready-a vachiruppan
✅ Customer varum bodhu than cup la pour panni kuduppan!
✅ Tea kada la tea kadaikkama iruka chance illa!
🔥 Ithu dhan Generator!
✅ On-demand data generate pannum
✅ Memory use pannama work pannum!


def tea_shop():
    while True:
        yield "☕ Hot Tea Ready!"  # Yield keeps the function alive!

tea = tea_shop()

print(next(tea))  # First cup
print(next(tea))  # Second cup
print(next(tea))  # Third cup

☕ Hot Tea Ready!
☕ Hot Tea Ready!
☕ Hot Tea Ready!

🔥 Tea kada owner range-ku irukingada! 🔥








📌 3. What is a Generator?
💡 Generator na enna?
Iterator la __iter__() and __next__() methods manually implement pannanum.
💡 Generator simplifies this by using yield instead of return.


🎯 Real-Life Example 2 – Borewell Water Supply 🚰
🏡 Situation:

Village la borewell water supply epdi irukum?
Motor ON pannumbodhu water varum, OFF pannumbodhu stop aagum.
Every time motor start panna water new-a generate aagum.
🔹 This is exactly how Generators work!
✅ Water full-a store pannamala, request ku thaan provide pannum.
✅ Memory-efficient, on-demand execution.





def borewell_water():
    yield "💧 Water Flowing..."
    yield "💧 Water Flowing..."
    yield "💧 Water Flowing..."
    yield "⛔ Water Stopped!"

tap = borewell_water()
print(next(tap))  # Water ON
print(next(tap))  # Water ON
print(next(tap))  # Water ON
print(next(tap))  # Water Finished!

💧 Water Flowing...
💧 Water Flowing...
💧 Water Flowing...
⛔ Water Stopped!

🚀 No need for __iter__() and __next__(), yield automatically handles everything!


!

📌 4. Difference Between Iterators & Generators
Feature	Iterator	Generator
Definition	Manually implements __iter__() and __next__()	Uses yield keyword
Complexity	More complex	Simple and clean
Memory Usage	Stores all elements in memory	Generates items one-by-one (less memory usage)
Performance	Slower	Faster
Example Use Case	Reading a file line by line	Generating infinite numbers



🎯 5. Real-World Example – Generating Infinite Lottery Numbers 🎟️
Scenario:

Lottery numbers random-a generate aaganum.
Each time function call panna new number generate aaganum.


import random

def lottery_numbers():
    while True:
        yield random.randint(100000, 999999)  # Generate 6-digit lottery number

lottery = lottery_numbers()
print(f"🎟️ Your Lottery Number: {next(lottery)}")  # Generate 1st Lottery Number
print(f"🎟️ Your Lottery Number: {next(lottery)}")  # Generate 2nd Lottery Number


🎟️ Your Lottery Number: 739401
🎟️ Your Lottery Number: 256987

✅ Memory-efficient & efficient for real-time use cases!


🔥 6. Interview Questions & Answers
❓ 1. What is the difference between return and yield?
Feature	return	yield
Function Type	Normal function	Generator function
Memory Usage	Stores entire result in memory	Generates values on demand
Execution	Runs once	Can pause & resume



❓ 2. What happens if next() is called on an exhausted generator?
💡 Throws StopIteration error!

def simple_gen():
    yield 1
    yield 2

g = simple_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # ❌ Error

💡 Fix: Handle using try-except

❓ 3. When should we use Generators?
✅ When we need large data processing (like reading large files, infinite sequences, etc.)
✅ When memory efficiency is important
✅ For real-time streaming applications (logs, live data processing, etc.)


🚀 Final Recap
✅ Iterators – Manually implement __iter__() & __next__()
✅ Generators – Use yield for easy iteration
✅ Iterators store data, Generators produce on demand (memory-efficient)
✅ Use cases: Reading files, infinite sequences, OTP generation, real-time data processing

🔥 Enna da, super-a purinjiruchu la? Next Topic venuma? 😎🔥

