#w.a.p.p to print prime numbers from 1 to n
n = int(input("Enter the number: "))
def prime2(a,k):
    if a!=0:
        c = 0
        for i in range(a):
            if k%(i+1)==0:
                c = c+1
        if(c==2):
            print(f"{k} is prime")
        return prime2(a-1,k+1)
    else:
        return
prime2(n,2)