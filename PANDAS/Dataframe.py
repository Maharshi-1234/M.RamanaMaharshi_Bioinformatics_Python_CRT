import pandas as pd
Data = (
    {'Std1':'Student',
    'Name':'Vignan',
    'Branch':'BI',
    'ID':'123',
    'Skills':['Python','DSA','SQL','C']
    },
    {'Std2':'Student',
    'Name':'University',
    'Branch':'CSE',
    'ID':'467',
    'Skills':['DSA','SQL','C']
    }
)
Data = pd.DataFrame(Data)
print(Data)
print(type(Data))