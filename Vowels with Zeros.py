#write a python program to read a string as input from the user and replace all Vowels with Zeros
str = input("Enter a String : ")
replaced = " "
for i in str:
    if i in 'AEIOUaeiou':
        replaced += '0'
    else:
        replaced += i
print(replaced)