
# quest-1 : Variable and Data types
# Create a variable called Name, Age, and Student
Name = "Abdullah" #string
Age = 27 #int
Student = True #bool 

# Print the type of each variable
print(type(Name))
print(type(Age))
print(type(Student))

# quest 2 : Arithmetic operations
print(27+3)
print(27-3)
print(27*3)
print(27/3)

# quest 3 : Comparison operations
Age = 27
if Age > 18:
    print("an adult")
else:
    print("not an adult")

# quest 4 : Logical operations

# Define two conditions
is_raining = True
has_umbrella = False

# Demonstrate 'and' operation
if is_raining and has_umbrella:
    print("You can go outside without getting wet")
else:
    print("You might get wet")

# Demonstrate 'or' operation
if is_raining or has_umbrella:
    print("You can consider going outside")
else:
    print("It's safe to stay indoors")

# Demonstrate 'not' operation
if not has_umbrella:
    print("You should carry an umbrella")

# quest 5 : Assignment operations
# Initialize a variable
x = 10
# Perform various assignment operations
x += 5  
print(x)  
x -= 3  
print(x)  
x *= 2  
print(x)  
x /= 4  
print(x)  

# quest 6 : Identity operations
# Initialize two variables
a = 10
b = 20
# Check identity using 'is' operator
print(a is b)  
# Check identity using 'is not' operator
print(a is not b)  

# quest 7 : Membership operations
# Initialize a list
my_list = ['dhaka', 'chittagong', 'rajshahi']
# Check membership using 'in' operator
print("dhaka" in my_list)
# Check membership using 'not in' operator
print("sylhet" not in my_list) 


