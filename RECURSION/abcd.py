N=int(input("Enter the value of n:"))
i=0
def NaturalNumber(N,i):
    i=i+1
    if N==0:
        return
    NaturalNumber(N-1,i)
    print(f" {i} Method Call")
NaturalNumber(N,i)