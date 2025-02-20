# Declaring and Using Integers

# Python automatically recognizes numbers without decimals as integers.

# Declaring integer variables
x = 10
y = -5
z = 1000

print(x, y, z)  
# Output: 10 -5 1000

print(type(x))  
# Output: <class 'int'>

# 💡 Key Points:
# ✔ No need to define the type explicitly (int x = 10; is NOT required like in C, Java).
# ✔ Python dynamically assigns the type based on the value.


# 2️⃣ Integer Operations (Arithmetic)
# Integers support basic arithmetic operations.

a = 15
b = 4

print(a + b)   # Addition → 19
print(a - b)   # Subtraction → 11
print(a * b)   # Multiplication → 60
print(a / b)   # Division (Result is float) → 3.75
print(a // b)  # Floor Division → 3 (Removes decimal part)
print(a % b)   # Modulus (Remainder) → 3
print(a ** b)  # Exponentiation (15^4) → 50625


# 3️⃣ Large Integers in Python
# Python supports arbitrarily large integers, meaning there is no fixed size limit (like int in C or Java).


big_num = 987654321987654321987654321
print(big_num)  
# Output: 987654321987654321987654321
print(type(big_num))  
# Output: <class 'int'>

# ❌ Invalid Conversion: Trying to convert a non-numeric string will raise an error.


# 5️⃣ Checking if a Variable is an Integer
# You can check if a variable is an integer using isinstance().

x = 50
print(isinstance(x, int))  # Output: True

y = 3.14
print(isinstance(y, int))  # Output: False


# 6️⃣ Integer Comparisons
# Python allows comparing integers using standard comparison operators.

a = 10
b = 20

print(a == b)  # False (10 is not equal to 20)
print(a != b)  # True  (10 is not equal to 20)
print(a > b)   # False
print(a < b)   # True
print(a >= 10) # True
print(b <= 25) # True

# 7️⃣ Bitwise Operations on Integers
# Python provides bitwise operations to work with binary representations of integers.

a = 5   # Binary:  101
b = 3   # Binary:  011

print(a & b)   # AND → 1 (Binary: 001)
print(a | b)   # OR  → 7 (Binary: 111)
print(a ^ b)   # XOR → 6 (Binary: 110)
print(~a)      # NOT → -6 (Two’s complement)
print(a << 1)  # Left Shift  (5 * 2) → 10
print(a >> 1)  # Right Shift (5 // 2) → 2



# 8️⃣ Integer Memory Management in Python
# Python optimizes memory usage for small integers (-5 to 256) by caching them.

a = 100
b = 100
print(a is b)  # Output: True (Same memory location)

x = 1000
y = 1000
print(x is y)  # Output: False (Different memory locations)


# 🔟 Random Integers (Generating Random Numbers)
# To generate random integers, use the random module.

import random
print(random.randint(1,100))
print(random.ranrange(1,100,5))


# Summary
# ✔ Python integers are whole numbers (positive, negative, zero)
# ✔ Supports arithmetic, comparison, and bitwise operations
# ✔ No fixed size (supports large numbers)
# ✔ Type conversion possible (float → int, str → int, bool → int)
# ✔ Supports binary, octal, and hexadecimal representations
# ✔ Efficient memory handling for small numbers
# ✔ Can generate random integers using random.randint()




