'''Write a Python Program to read the length of the string as input from 
the user and print all Binary strings of length N.
'''
def generate_binary_no_backtrack(n):
    result = '0' * n 
    print(result)

generate_binary_no_backtrack(3)
#With Backtracking
print("With Backtracking")
def generate_binary_backtrack(n, current=""):
    if len(current) == n:
        print(current)
        return
    #Choose "0"
    generate_binary_backtrack(n, current + '0')
    #Choose "1"
    generate_binary_backtrack(n, current + '1')
generate_binary_backtrack(3)