import pandas as pd
import datetime
df = pd.read_csv("500410.csv")
df['Date'] = pd.to_datetime(df['Date'])
all_years = df['Date'].dt.year.unique()
all_data = {'Date': [], "Growth": []}
for i in all_years:
    for j in range(1,13):
        data = df[(df['Date'].dt.year == i) & (df['Date'].dt.month == j)]
        for q in data['Date']:
            q = q.date()
            a = 1
            while True:
                p = q - datetime.timedelta(days=a)
                if (df['Date'] == p).any():
                    break
                elif q == min(df['Date'].dt.date):
                    break
                else:
                    a = a + 1
            try:
                x = df[q == df['Date']].iloc[0, 4]
                y = df[p == df['Date']].iloc[0, 4]
                all_data['Date'].append(q)
                all_data['Growth'].append(((y-x)/y)*100)
            except:
                continue

all_data = pd.DataFrame(all_data)
all_data.to_csv("D-GROWTH.csv")
