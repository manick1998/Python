🔹 Concept
Python oru datatype-a vera datatype-ku automatically convert panidum if necessary. Intha process-a implicit type conversion nu solvom.

🏠 Real-Life Example
💡 Situation:
Nee tea pot-la milk heat panna pora. Tea pot-la konjam hot water already iruku. Idhukku milk add panna enna aagum? Milk automatic-a heat aagum.

🔹 Tea Pot → int (Water - 50°C)
🔹 Milk → float (Room Temperature - 25.5°C)
🔹 Final Mixture → float (Average Temperature - 35.75°C)

Appadiye, Python-layum small datatype (int) big datatype (float)-kku convert aagum without issue.




# Integer + Float => Float
a = 10   # int
b = 5.5  # float
c = a + b  # int + float → float
print(c)    # 15.5
print(type(c))  # Output: <class 'float'>
👉 Python automatically int-ah float-ah convert pannidum!



2️⃣ Type Casting (Explicit Conversion) – Manual Conversion 🛠
🔹 Concept
Ellathayum Python automatic-a convert panna mudiyadhu. Sometimes, namma manual-a datatype convert pannanum. Idhuku Explicit Type Casting use pannuvom.


🏠 Real-Life Example
💡 Situation:
Nee foreign country-ku poi ATM la money withdraw panna pora. But un ATM card INR (₹) la iruku. Aana foreign country la only USD ($) accept pannum. So, nee INR → USD convert pannanum.

🔹 INR (String Format - "5000") → USD (Integer - 60$)

Same way, Python-kum datatype matha theriyadhu. Namma matha sollanum.

✅ Example Code – Explicit Type Conversion
🔹 String to Integer Conversion


num_str = "100"   # String format
num_int = int(num_str)  # Converting to Integer
print(num_int)    # Output: 100
print(type(num_int))  # Output: <class 'int'>
👉 Decimal part remove aagum! Round pannidathu!

🔹 Integer to String Conversion
num = 123  
num_str = str(num)  
print(num_str)  # Output: "123"
print(type(num_str))  # Output: <class 'str'>


🔥 3 Real-Time Use Cases
🏢 1. Age Verification System
💡 Scenario: Website signup la Age Check iruku. User age string format la kuduthurkaan, but compare panna int format venum.


user_age = input("Enter your age: ")  # User input (string)
user_age = int(user_age)  # Convert to integer

if user_age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")
👉 String input-a int-ah convert panni logic apply pannuvom!

💰 2. Online Payment System
💡 Scenario: Bank la ₹500 balance iruku. User ₹100 withdraw panna pora. But backend balance string format la iruku.


balance = "500"  # Bank balance stored as string
withdraw = 100   # Withdraw amount

balance = int(balance)  # Convert balance to integer
balance -= withdraw  # Deduct amount

print("Remaining Balance:", balance)  


🚀 3. Sensor Data Processing
💡 Scenario: IoT sensor temperature data float format la varum. But CSV file la only integer format save pannanum.

temperature = 36.7  # Sensor reading (float)
temperature_int = int(temperature)  # Convert to int

print(f"Saving Temperature: {temperature_int}°C")  





🎯 Interview Questions & Answers
❓ 1. Difference between Type Conversion & Type Casting?
✅ Type Conversion → Python automatic-a datatype convert pannum. Example: int + float = float
✅ Type Casting → Namma manual-a datatype change pannalam using int(), float(), etc.

❓ 2. What happens when you convert float to int?
✅ Decimal part remove aagum. Example: int(5.99) → 5

❓ 3. How do you convert a number to a string?
✅ Using str(). Example: str(123) → "123"



 Summary
✅ Type Conversion – Python automatic-a convert pannum
✅ Type Casting – Namma manual-a convert pannalam
✅ Real-world examples – Bank, Age verification, IoT sensor
✅ Interview preparation – Common questions & answers

இப்போ Type Conversion & Type Casting concept 100% crystal clear! 😎🔥 Doubt irundha kelunga! 🚀