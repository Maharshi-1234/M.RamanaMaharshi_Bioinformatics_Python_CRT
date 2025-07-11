'''
Altaf has recently learned about number bases and is becoming fascinated.
Altaf learned that for bases greater than ten, new digit symbols need to be introduced, 
and that the convention is to use the first few letters of the English alphabet. For 
example, in base 16, the digits are 0123456789ABCDEF. Altaf thought that this is 
unsustainable; the English alphabet only has 26 letters, so this scheme can only 
work up to base 36. But this is no problem for Altaf, because Altaf is very creative 
and can just invent new digit symbols when she needs them. (Altaf is very creative.)
Altaf also noticed that in base two, all positive integers start with the digit 1! 
However, this is the only base where this is true. So naturally, Altaf wonders: Given 
some integer N, how many bases b are there such that the base-b representation of N 
starts with a 1?
INPUT FORMAT :
----------------
The first line of the input contains an integer T denoting the number of test cases. 
The description of T test cases follows.
Each test case consists of one line containing a single integer N (in base ten).
OUTPUT FORMAT :
------------------
For each test case, output a single line containing the number of bases b, or 
INFINITY if there are an infinite number of them.
CONSTRAINTS :
----------------------
1 <= T <= 10^5
0 <= N < 10^12
SAMPLE INPUT :
---------------
4
-----------------
6
9
11
24
----------------
SAMPLE OUTPUT :
4
7
8
14
'''
