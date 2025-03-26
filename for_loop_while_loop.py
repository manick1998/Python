🔥 Python Looping (for, while, nested loops)

 Example:

Mobile password wrong ah type panna, 3 attempts varaikum try panna kodukum.
Petrol tank full aagura varaikum fill pannuvom.
School la students ku attendance check pannuvom.


🔥 Python has 2 main types of loops:
1️⃣ for loop – Fixed number of times execute aagum.
2️⃣ while loop – Condition satisfy aagura varaikum execute aagum.
3️⃣ Nested Loops – Loop inside another loop.


🔥 2. for Loop – Count-Based Looping
📖 Real-Life Example 1 – Counting Students in a Class
Scenario:

1st standard la 5 students irukanga.
Teacher each student ku ID print pannanum.
Fixed count iruku → So for loop best.


for student in range(1, 6):  
    print(f"📝 Student ID: {student}")  


📝 Student ID: 1
📝 Student ID: 2
📝 Student ID: 3
📝 Student ID: 4
📝 Student ID: 5



📖 Real-Life Example 2 – TV Channel Switching
Scenario:

Remote la channel button press panna, channel 1 to 5 varaikum switch aagum.
Each channel print panna for loop use pannuvom.
🔥 Python Code:
    
    
    
channels = ["Sun TV", "Vijay TV", "Zee Tamil", "Jaya TV", "Colors Tamil"]

for channel in channels:
    print(f"📺 Switching to {channel}")


📺 Switching to Sun TV
📺 Switching to Vijay TV
📺 Switching to Zee Tamil
📺 Switching to Jaya TV
📺 Switching to Colors Tamil



🔥 3. while Loop – Condition-Based Looping
📖 Real-Life Example 3 – ATM Money Withdrawal
Scenario:

ATM la money withdraw panna vendiyadhu.
Balance 500 Rs. irukku, withdrawal limit reach aagura varaikum withdraw panna vendiyadhu.


balance = 500  
withdraw = 100  

while balance > 0:  
    print(f"💰 Rs.{withdraw} withdrawn. Remaining balance: Rs.{balance - withdraw}")  
    balance -= withdraw  

print("❌ No balance left!")  


📖 Real-Life Example 4 – Password Retry System
Scenario:

ATM password 3 times thappu panna account lock aagum.
Wrong attempt 3 times panna while loop stop aagum.
🔥 Python Code:

password = "1234"
attempts = 0

while attempts < 3:
    user_input = input("🔑 Enter PIN: ")
    if user_input == password:
        print("✅ Access Granted")
        break
    else:
        print("❌ Wrong PIN!")
        attempts += 1

if attempts == 3:
    print("⛔ Account Locked!")

    
    
    
🔑 Enter PIN: 1111
❌ Wrong PIN!
🔑 Enter PIN: 2222
❌ Wrong PIN!
🔑 Enter PIN: 3333
❌ Wrong PIN!
⛔ Account Locked!



🔥 4. Nested Loops – Loop Inside a Loop
📖 Real-Life Example 5 – Cricket Scoreboard Update
Scenario:

IPL match la each over ku 6 balls irukum.
For each over, each ball ku score print panna vendiyadhu.



for over in range(1, 3):  # 2 overs
    print(f"🏏 Over {over}")
    for ball in range(1, 7):  # 6 balls in each over
        print(f"🎯 Ball {ball}: Scored {ball * over} runs")
🏏 Over 1
🎯 Ball 1: Scored 1 runs
🎯 Ball 2: Scored 2 runs
...
🏏 Over 2
🎯 Ball 6: Scored 12 runs



📖 Real-Life Example 6 – Stop at First Discount Product
Scenario:

Supermarket la 10 products check panna vendiyadhu.
Discount product kidaichuduna stop pannum (break).
🔥 Python Code:
    
products = ["Rice", "Oil", "Milk", "Discounted Soap", "Shampoo"]

for product in products:
    print(f"🔍 Checking {product}")
    if "Discount" in product:
        print(f"🎉 {product} - Offer available! Stopping search.")
        break


🔍 Checking Rice
🔍 Checking Oil
🔍 Checking Milk
🔍 Checking Discounted Soap
🎉 Discounted Soap - Offer available! Stopping search.



📖 Real-Life Example 7 – Skip Sundays in Work Plan (continue)
Scenario:

Monday to Sunday work schedule irukku.
Sunday ku rest day, so continue use panni skip pannanum.


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    if day == "Sunday":
        print("⛔ Rest day, skipping work!")
        continue
    print(f"📅 Working on {day}")


📅 Working on Monday
📅 Working on Tuesday
📅 Working on Wednesday
📅 Working on Thursday
📅 Working on Friday
📅 Working on Saturday
⛔ Rest day, skipping work!




🔥 Interview Questions & Answers
❓ 1. Difference between for and while loop?
Feature	for Loop	while Loop
Use Case	Fixed number of iterations	Condition-based iteration
Example	for i in range(5):	while i < 5:
    
    
    
❓ 2. What happens if we don’t update the condition in while loop?

🚫 Infinite Loop aagum!
🔥 Example:
    
count = 0
while count < 5:
    print(count)  # Condition update panna illa, so infinite loop!

❓ 3. Can we use else with loops?
✅ Yes!
🔥 Example:
    
for i in range(3):
    print(i)
else:
    print("Loop finished without `break`")


0
1
2
Loop finished without `break`


🚀 Final Recap
✅ for Loop – Count-based iteration
✅ while Loop – Condition-based iteration
✅ Nested Loop – Loop inside a loop
✅ break – Stops loop immediately
✅ continue – Skips current iteration
✅ Infinite Loop – Possible using while True

🔥 Any doubts? Next topic venuma? 😎🔥





