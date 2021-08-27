import pandas as pd
q = pd.read_csv("social.csv", sep=" ")
#print(q[(q["Gender"] == "Female") & (q["Purchased"] ==  1)])
#print(q[(q["Gender"] == "Female") & (q["Purchased"] == 1)][["User", "Gender"]])
#print(q["Purchased"].value_counts())
# print(q.loc[0, ["Gender"]])
# print(q.iloc[1, 1])
print(q.iloc[2:26, 1:3])
