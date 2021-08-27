import pandas as pd
df1 = pd.read_csv("Movie_Id_Titles.csv")
df2 = pd.read_csv("file.tsv", sep='\t')
df2.columns = ["user_id", "item_id", "rating", "timestamp"]
df = df1.merge(df2, on="item_id")
print(df)
print(df.corr())
