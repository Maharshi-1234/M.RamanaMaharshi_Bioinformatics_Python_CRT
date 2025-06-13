#write a python program to read a string as a input from the user[including spaces and print the string by trimming the spaces]
Input = input("Enter the String :")
print(f"User Entered String :{Input}")
s=str(Input.split())
print("String without spaces : {s}")