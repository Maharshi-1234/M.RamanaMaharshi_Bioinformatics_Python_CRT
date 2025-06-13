#write a python program to read Mail_ID as input from the user and convert into the list and print it in seperately
Mail_Id=input("Enter the Mail_Id :")
List=Mail_Id.split('@')
print(f"User Name : {List[0]}")
org=List[1]
List=org.split('.')
print(f"Org Name :{List[0]}")