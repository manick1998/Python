# Python Float (float) – A-Z Detailed Explanation with Code

# A float (float) in Python represents a decimal number (floating-point number). It can be positive, negative, or zero, with a fractional part.

# 1️⃣ Declaring and Using Floats
# A float is any number that contains a decimal point.

# Float numbers
x = 10.5  
y = -3.14  
z = 0.0  

print(x, y, z)  
# Output: 10.5 -3.14 0.0

print(type(x))  
# Output: <class 'float'>

# 💡 Key Points:
# ✔ Any number with a decimal point is a float.
# ✔ Python automatically detects floats without needing explicit declaration.


2️⃣ Scientific Notation in Floats
Python supports scientific notation (E-notation) for very large or small numbers.

# Using scientific notation
num1 = 1.2e3   # 1.2 × 10³ = 1200.0
num2 = 2.5E-4  # 2.5 × 10⁻⁴ = 0.00025

print(num1)  # Output: 1200.0
print(num2)  # Output: 0.00025


💡 e or E means "times 10 to the power of".

3️⃣ Float Arithmetic Operations

a = 5.5
b = 2.2

print(a + b)   # Addition → 7.7
print(a - b)   # Subtraction → 3.3
print(a * b)   # Multiplication → 12.1
print(a / b)   # Division → 2.5
print(a // b)  # Floor Division → 2.0 (Removes decimal part)
print(a % b)   # Modulus → 1.1 (Remainder)
print(a ** b)  # Exponentiation → 5.5^2.2 = 42.81


💡 Difference Between / and //:

/ returns float (5.5 / 2.2 → 2.5).
// removes decimal part (5.5 // 2.2 → 2.0).

4️⃣ Converting Other Data Types to Float (Type Casting)

# Integer to Float
num_int = 10
num_float = float(num_int)
print(num_float)  # Output: 10.0

# String to Float
num_str = "3.14159"
num_float = float(num_str)
print(num_float)  # Output: 3.14159

# Boolean to Float
print(float(True))   # Output: 1.0
print(float(False))  # Output: 0.0


❌ Invalid Conversion: Trying to convert a non-numeric string will raise an error.

# float("hello")  ❌ ValueError: could not convert string to float


5️⃣ Checking if a Variable is a Float

x = 3.14
print(isinstance(x, float))  # Output: True

y = 10
print(isinstance(y, float))  # Output: False

6️⃣ Rounding Floats
To round a float to a specific number of decimal places, use round().


num = 3.14159

print(round(num, 2))  # Output: 3.14 (Rounded to 2 decimal places)
print(round(num, 0))  # Output: 3.0

7️⃣ Formatting Floats
You can format floats using f-strings or format().

pi = 3.14159

# Using f-strings
print(f"Value of pi: {pi:.2f}")  # Output: Value of pi: 3.14

# Using format()
print("Value of pi: {:.3f}".format(pi))  # Output: Value of pi: 3.142


💡 :.2f limits to 2 decimal places.


8️⃣ Floating-Point Precision Issues
Floats in Python may have small precision errors due to how computers store decimal numbers

a = 0.1 + 0.2
print(a)  
# Output: 0.30000000000000004 (NOT exactly 0.3)

To fix precision errors, use the decimal module.

from decimal import Decimal

a = Decimal('0.1') + Decimal('0.2')
print(a)  
# Output: 0.3 (Correct precision)


Summary
✔ Floats represent decimal numbers (3.14, -5.5, 0.0).
✔ Supports arithmetic operations (+, -, *, /, **, %, //).
✔ Can be converted from integers, strings, booleans (float(10) → 10.0).
✔ Formatting ({:.2f}) controls decimal places.
✔ Handles large/small numbers using scientific notation (1.2e3 → 1200.0).
✔ Precision issues can be fixed using decimal module.
✔ Infinity (inf) and NaN (nan) are supported.
✔ Generate random floats using random.uniform() and random.random()



