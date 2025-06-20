#w.a.p.p to print square numbers from n to 1
n = int(input("Enter the number: "))
def square(a):
    if a!=0:
        print(f"Square of {a} is {a*a}")
        return square(a-1)
    else:
        return
square(n)