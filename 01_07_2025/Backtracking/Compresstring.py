'''
## Problem Statement:
Given a string s of lowercase letters, compress it by replacing sequences of repeated 
characters with the character followed by the count. Return the compressed string only if it's shorter than the original, 
else return the original.
## Input:
A string s (1 <= |s| <= 10s)
## Output:
Compressed string or original string if compression doesn't reduce size
## Sample Test Cases:
Example 1:
### Input:
aaabbccdee  
### Output:  
a3b2c2d1e2  
'''
s = input("Enter a lowercase string: ")
res = ''
for ch in s:
    if ch not in res:
        res += ch + str(s.count(ch))
print(res)