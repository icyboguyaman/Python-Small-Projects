import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO:- load data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

print("Age:", (train_df['Age'].isnull().sum() / len(train_df[:])) * 100)
print("Cabin:", (train_df['Cabin'].isnull().sum() / len(train_df[:])) * 100)
print("Embarked:", (train_df['Embarked'].isnull().sum() / len(train_df[:])) * 100)

#sns.countplot(train_df['Survived'], data=train_df, hue='Pclass')
#sns.countplot(train_df['Survived'], data=train_df, hue='Sex')
#sns.distplot(train_df['Age'].dropna(), kde=False, bins=30, color='Green')

#sns.boxenplot(x='Pclass', y='Age', data=train_df)

#plt.show()

print(train_df['Age'])

# for temp in train_df[['PassengerId', 'Pclass', 'Age']].values:
#     pid = temp[0]
#     p = temp[1]
#     a = temp[2]
#     if pd.isnull(a):
#         train_df.loc[pid-1, 'Age'] = train_df[train_df["Pclass"] == p]["Age"].mean()
#     else:
#         train_df.loc[pid-1, 'Age'] = train_df.loc[pid-1, 'Age']
#
# print(train_df['Age'])
def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train_df[train_df["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train_df["Age"] = train_df[["Age", "Pclass"]].apply(add_age,axis=1)

print(train_df['Age'])
print(train_df['Age'].isnull().sum())
