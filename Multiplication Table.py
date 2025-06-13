#Write the Python Program to build a function which prints the multiplication table of N
def Multiplication_Table(Num):
    for i in range(10):
        print(f"{Num} * {Num+i} =",Num*(i+1))
n = int(input("Enter a Number: "))
Multiplication_Table(n)