#write a python program to read the string as a input from the user and 
#1)reverse the string
#2)convert the string into lowercase
#3)convert the string into uppercase
#4)convert the characters of string to lowercase if it is in uppercase 
#5)convert the characters of string to uppercase if it is in lowercase
#6)check if the string is starting with the letter A and 
#7)Print the count of the characater A from the given string and replace all P's to J
str=input("Enter the String : ")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('P'))
print(str.count('P'))
str=str.lower()
print(str.replace('p','j'))