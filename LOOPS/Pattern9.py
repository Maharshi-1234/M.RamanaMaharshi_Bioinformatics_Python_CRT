'''
      S                   4
    I S H               3 4 5
  R I S H N           2 3 4 5 6
K R I S H N A       1 2 3 4 5 6 7
  R I S H N           2 3 4 5 6
    I S H               3 4 5
      S                   4
'''
Str = "KRISHNA"
Length = len(Str)
Mid=Length//2
for i in range(Length):
    for j in range(Length):
        if(j==i):
            print(f"{Str[j]-i-1}", end = " ")
    print()