#write a python program to take name as input from the user(including prefix as Mr/Mrs) and print the gender
#classification of the name on basis of prefix
str = input("Enter Your Name with prefix (Mr/Ms): ")
if str.startswith('Ms'):
    print("Female")
else:
    print("Male")