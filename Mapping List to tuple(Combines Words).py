#write a python program to declare a list of words and declare a tuple of words and map it to print the combined words
n = int(input("Enter the no.of words that you would like to find: "))
List=['Marker','Water','Wrist','Bread','class','Home','Jim','Black','Crack']
Tuple= ('Pen','Bottle','Watch','Jam','Room','Theatre','Jam','Board','Jack')
i=1
while(i<=n):
    word=input("Enter the word:")
    index=List.index(word)
    print(f"{word}--{Tuple[index]}")
    i+=1