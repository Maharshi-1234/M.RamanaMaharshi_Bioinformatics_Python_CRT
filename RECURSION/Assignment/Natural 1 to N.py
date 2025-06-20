#Write a python program to print natural numbers from 1 to N
N=int(input("Enter the value of n: "))
def NaturalNum(N):
    if N==0:
        return 
    NaturalNum(N-1)
    print(N)
NaturalNum(N)