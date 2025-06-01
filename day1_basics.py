# day1_basics.py

# 1. Variables and data types
name = "Cloudera"
year = 2025
is_active = True
print(f"Welcome to {name}, Year: {year}, Active: {is_active}")

# 2. User input
user = input("Enter your name: ")
print("Hello", user)

# 3. If-Else
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Excellent!")
elif score >= 75:
    print("Good")
else:
    print("Needs Improvement")

# 4. Loops
print("Even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 5. Function
def greet(name):
    return f"Hello, {name}! Welcome to Python training."

print(greet(user))

# Variable declaration
company = "Cloudera"      # str
year = 2025               # int
ram_gb = 16.0             # float
is_cloud = True           # bool

print(type(company))   # <class 'str'>
print(type(ram_gb))    # <class 'float'>
