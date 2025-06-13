#write a python prpgram to read a list of characaters as input from the user and convert into word 
#and seperate them
size = int(input("Enter the Length of List :"))
char_list = []
for i in range(size):
    ch = input("Enter the characters :")
    char_list.append(ch)
print(char_list)
str = "".join(char_list)
print(str)