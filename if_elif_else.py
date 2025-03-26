✅ Conditional Statements (if, elif, else) – Full Postmortem in Detail

🔥 This is one of the most important topics in Python!
🔥 Interviews, real-time coding, and logic-building la if-else romba mukkiyam!
🔥 Doubt irundha kooda ipo clear aagidum! 😎

🔥 1. What is a Conditional Statement?
📌 Definition: Condition check panni oru decision edukka if-else use pannuvom.
📌 Example: If rain varudhu na umbrella edukku, illana edukka vendaam.


🛠 Python la 3 types of conditional statements iruku:
✅ if → Condition true na execute aagum.
✅ if-else → True na one block, False na another block execute aagum.
✅ if-elif-else → Multiple conditions check pannum.


💡 Edhukku use pandrom?
Oru program decision edukkanum na, conditions use pannanum! Example:

ATM Example → Balance irundha withdrawal panna vidanum, illana "Insufficient Balance" solanum.
E-Commerce → ₹500 mela purchase panna free delivery kudukanum.
Exam Result → Mark check panni "Pass" or "Fail" decide pannanum.
🔥 Key Keywords:
✅ if → Condition true na execute agum
✅ elif → Multiple conditions check pannum
✅ else → Above conditions ellam false na, default block run agum



✅ 1. Basic if Condition

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")


🔹 User 20 kudutha: "You are eligible to vote."
🔹 User 15 kudutha: No output (condition false, so nothing prints)


✅ 2. if-else Example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")


🔹 User 20 kudutha: "You are eligible to vote."
🔹 User 15 kudutha: "You are NOT eligible to vote."


✅ 3. if-elif-else Example (Multiple Conditions)
🔹 Example: Grade Calculation System


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F (Fail)")


💡 Working:

90+ → A+
80+ → A
70+ → B
60+ → C
Below 60 → Fail
Example Runs:
🔹 User 85 kudutha → "Grade: A"
🔹 User 40 kudutha → "Grade: F (Fail)"


✅ 4. Nested if Example (if inside if)
🔹 Example: ATM Withdrawal System

balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    if withdraw % 100 == 0:  # Check if amount is multiple of 100
        balance -= withdraw
        print(f"Transaction successful! Remaining balance: {balance}")
    else:
        print("Amount should be in multiples of 100!")
else:
    print("Insufficient balance!")


👉 User 2500 kudutha, output → "Transaction successful! Remaining balance: 2500"** 👉 **User 3700kudutha, output → "Amount should be in multiples of 100!"** 👉 **User6000` kudutha, output → "Insufficient balance!"

✅ 5. Short-Hand if Statement (One-line if condition)

age = int(input("Enter your age: "))
if age >= 18: print("You can vote.")


🔥 One-liner code: No need {} or indentation.

✅ 6. Short-Hand if-else (Ternary Operator)

age = int(input("Enter your age: "))
print("Eligible" if age >= 18 else "Not Eligible")


👉 User 20 kudutha → "Eligible"
👉 User 15 kudutha → "Not Eligible"



🔥 3 Real-Life Examples
🏪 1. Shopping Cart Discount System
💡 Scenario: ₹500 mela buy panna 10% discount kudukanum.

amount = float(input("Enter your total bill: "))

if amount >= 500:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"You got ₹{discount} discount! Final Bill: ₹{final_amount}")
else:
    print(f"No discount. Final Bill: ₹{amount}")


👉 User 600 kudutha → "You got ₹60 discount! Final Bill: ₹540"
👉 User 450 kudutha → "No discount. Final Bill: ₹450"



🎓 2. University Admission Eligibility
💡 Scenario: Student 12th mark >= 75% irundha admission eligible.


marks = float(input("Enter your 12th percentage: "))

if marks >= 75:
    print("You are eligible for admission.")
else:
    print("Sorry, you are not eligible.")


👉 User 80% kudutha → "You are eligible for admission."
👉 User 60% kudutha → "Sorry, you are not eligible



🚦 3. Traffic Signal System
💡 Scenario:

Red → "Stop"
Yellow → "Slow down"
Green → "Go"


signal = input("Enter traffic light color: ").lower()

if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("SLOW DOWN!")
elif signal == "green":
    print("GO!")
else:
    print("Invalid color!")



👉 User Red kudutha → "STOP!"
👉 User Yellow kudutha → "SLOW DOWN!"
👉 User Green kudutha → "GO!"
👉 User Blue kudutha → "Invalid color!"

🎯 Interview Questions & Answers
❓ 1. Difference Between if and elif?
✅ if → First condition check pannum
✅ elif → Multiple conditions check pannum
✅ Example:


x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")

👉 Output: "Equal"




❓ 2. What is Short-Hand if-else?
✅ Answer: One-line if-else (Ternary Operator)

x = 5
print("Positive" if x > 0 else "Negative")


👉 Output: "Positive"



❓ 3. Can we use multiple elif conditions?
✅ Yes! Example:


temp = int(input("Enter temperature: "))

if temp > 30:
    print("Hot weather")
elif temp > 20:
    print("Warm weather")
elif temp > 10:
    print("Cool weather")
else:
    print("Cold weather")


👉 User 25 kudutha → "Warm weather"

🚀 Summary
✅ if – Single condition check
✅ if-else – True / False decision
✅ if-elif-else – Multiple conditions check
✅ Nested if – Condition inside another condition
✅ Short-Hand if – One-liner if
✅ Ternary Operator – One-liner if-else

🔥 Ippo if-elif-else topic 100% clear! 😎🔥 Doubt irundha kelunga! 🚀
