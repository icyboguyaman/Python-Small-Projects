import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
df = pd.read_csv("D-GROWTH.csv")
df['Date'] = pd.to_datetime(df["Date"])
all_years = df['Date'].dt.year.unique()
temp = {'Date': [], 'Growth': []}
for i in all_years:
    for j in range(12, 0, -1):
        data = df[(df['Date'].dt.year == i) & (df['Date'].dt.month == j)]
        try:
            last_date = max(data['Date'].dt.date)
            temp['Date'].append(last_date)
            temp['Growth'].append(data[data['Date'] == last_date].iloc[0, 2])
        except:
            continue
temp = pd.DataFrame(temp)
month_data = {'Date': [], 'Month Growth': []}
for i in range(len(temp)):
    month_data['Date'].append(temp['Date'][i])
    try:
        x = ((temp['Growth'][i+1] - temp['Growth'][i]) / temp['Growth'][i+1]) * 100
        month_data['Month Growth'].append(x)
    except:
        month_data['Month Growth'].append(temp['Growth'][i])
month_data = pd.DataFrame(month_data)
month_data.to_csv("M-Growth.csv")
sns.lineplot(x='Date', y='Month Growth', data=month_data, markers=True, dashes=False)
plt.show()
