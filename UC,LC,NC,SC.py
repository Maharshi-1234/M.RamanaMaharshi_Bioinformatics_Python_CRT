#write a python program to read a string as input from the user and print number of 
#1)count of uppercase letters
#2)count of lowercase letters
#3)count of numeric values
#4)count of special characters(space is also special character)
str = input("Enter the string: ")
uppercase_char = 0
lowercase_char = 0
num_values = 0
special_char = 0 
for ch in str:
    if ch.isupper():
        uppercase_char+=1
    elif ch.islower():
        lowercase_char+=1
    elif ch.isdigit():
        num_values+=1
    else:
        special_char+=1
print(f"Count of Uppercase Letters : {uppercase_char}")
print(f"Count of Lowercase Letters : {lowercase_char}")
print(f"Count of Numeric Values : {num_values}")
print(f"Count of Special Characters : {special_char}")