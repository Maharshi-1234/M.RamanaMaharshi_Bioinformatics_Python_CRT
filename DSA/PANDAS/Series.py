import pandas as pd
Num=['list of num',10,20]
print(pd.Series(Num))
Num_Series = pd.Series(Num, index=['i','ii','iii'])
print(Num_Series)