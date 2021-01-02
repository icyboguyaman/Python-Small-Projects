import numpy as np 
import pandas as pd 
import seaborn as sns   

df = pd.read_csv('/Users/icyboguy/Desktop/PYWork/data.csv')
print(df)

print(df.shape)

for col in df.columns:
    print(col)

print(df['Preferred Foot'])

l1=len(df[df['Preferred Foot']=='Left'])
r1=len(df[df['Preferred Foot']=='Right'])
print('Total no. of right foot players  :',l1)
print('Total no. of left foot players  :',r1)