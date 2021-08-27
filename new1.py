import pandas as pd
d = {"a": 5, "b": 10, "c": 12, "d":13}
x = pd.Series(d)
d = {"a": 5, "e": 10, "f": 13, "g": 14}
y = pd.Series(d)
df = pd.DataFrame({"a": x, "b": y, "a+b": x+y})
#print(df)
print(df[df['b'].isnull()].sum())
