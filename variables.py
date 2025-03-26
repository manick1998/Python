# 1. Declaring and Assigning Variables

# Assigning integer value
x = 10  
print(x)  # Output: 10

# Assigning float value
y = 3.14  
print(y)  # Output: 3.14

# Assigning string value
name = "Alice"  
print(name)  # Output: Alice




# 💡 Key Points:
# ✅ Python variables do not require a type declaration (int x = 10; is NOT needed).
# ✅ The variable type is inferred based on the assigned value.



# 2. Rules for Naming Variables
# Python has some rules for valid variable names:

# ✔ Valid variable names:
# ✅ Must start with a letter (a-z, A-Z) or an underscore (_)
# ✅ Can contain letters, digits (0-9), and underscores
# ✅ Case-sensitive (Name and name are different)

# ❌ Invalid variable names:
# ⛔ Cannot start with a digit (1variable = "wrong")
# ⛔ Cannot use spaces (my variable = "wrong")
# ⛔ Cannot use special characters ($, @, #, etc.)

# Correct variable names
age = 25  
_name = "John"  
user123 = "Alice"  

# Incorrect variable names
# 1name = "Error"  ❌ SyntaxError
# my variable = "Error"  ❌ SyntaxError
# name@ = "Error"  ❌ SyntaxError


# 3. Multiple Assignments
# Python allows assigning multiple variables in a single line.

# Assigning multiple variables in one line
a, b, c = 10, 20, 30
print(a, b, c)  # Output: 10 20 30

# Assigning the same value to multiple variables
x = y = z = 50  
print(x, y, z)  # Output: 50 50 50


# 4. Dynamic Typing in Python
# Python variables are dynamically typed, meaning they can change type during execution.

x = 100     # x is an integer
print(type(x))  # Output: <class 'int'>

x = "Hello"  # x is now a string
print(type(x))  # Output: <class 'str'>

x = 3.14    # x is now a float
print(type(x))  # Output: <class 'float'>



# 5. Type Casting (Explicit Conversion)
# You can convert variables from one type to another using type casting functions:

# Integer to String
num = 100
num_str = str(num)
print(num_str, type(num_str))  # Output: "100" <class 'str'>

# String to Integer
str_num = "50"
num_int = int(str_num)
print(num_int, type(num_int))  # Output: 50 <class 'int'>

# Float to Integer
pi = 3.99
pi_int = int(pi)
print(pi_int)  # Output: 3 (decimal part removed)


# 6. Global and Local Variables
# Local variables are declared inside a function and accessible only within that function.
# Global variables are declared outside a function and accessible anywhere in the script.

x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    print("Inside function:", x, y)  

my_function()
print("Outside function:", x)  
# print(y)  # This will cause an error (y is local)


# Tip: Use global keyword inside a function if you need to modify a global variable.

count = 0  # Global variable

def update():
    global count
    count += 1  # Modify global variable inside function
    print("Count inside function:", count)

update()
print("Count outside function:", count)  


# 7. Constants in Python
# Python does not have built-in constants, but by convention, constants are written in UPPERCASE.


PI = 3.14159  # Constant (by convention)
GRAVITY = 9.8
print(PI, GRAVITY)


# 8. Special Types of Variables
# a) None Type
# None represents the absence of a value (similar to null in other languages).

value = None
print(value, type(value))  # Output: None <class 'NoneType'>


# b) Boolean Variables
# A boolean variable stores True or False values.

is_active = True
is_completed = False
print(is_active, is_completed)  # Output: True False


# c) Complex Numbers
# Python supports complex numbers (a + bj format).

c_num = 3 + 5j
print(c_num.real, c_num.imag)  # Output: 3.0 5.0



# 9. Deleting a Variable
# Use del keyword to delete a variable.

x = 10
print(x)  # Output: 10
del x
# print(x)  # This will cause an error (NameError: name 'x' is not defined)

