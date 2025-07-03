'''Write a python program to check whether the user entered two strings are pangrams or not.'''
Str = input("Enter the String: ").upper()
Str = Str.replace(" ", "")
print(f"User Entered String : {Str}")
Str_set = set(Str)
alphabet_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
if alphabet_set.issubset(Str_set):
    print("Pangram")
else:
    print("Not a Pangram")
