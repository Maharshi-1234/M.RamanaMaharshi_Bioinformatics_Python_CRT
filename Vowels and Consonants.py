#write a program to take string as input 
#print the count of uppercase vowels 
#print the count of lowercase vowels 
#lowercase consonants
#count of uppercase consonants
str = input("Enter the string : ")
U_Vowels= L_Vowels = U_Consonants = L_Consonants = 0
for ch in str:
    if (ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if (ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print("the count of uppercase vowels is :",U_Vowels)
print("the count of lowercase vowels is :",L_Vowels)
print("the count of uppercase vowels is :",U_Consonants)
print("the count of lowercase vowels is :",L_Consonants)
