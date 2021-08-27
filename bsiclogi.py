import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO:- load data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# TODO:- remove all the nan values from data sets
# print(train_df.isnull().sum())
# sns.heatmap(train_df.isnull(),yticklabels=False,cbar=False)


# DATA ANALYSIS

# sns.countplot(x = 'Survived',hue='Pclass', data=train_df)
# sns.countplot(x = 'Survived',hue='Sex', data=train_df)
# sns.distplot(train_df['Age'].dropna(), kde=False, bins=30, color='Green')


# sns.boxplot(x='Pclass',y='Age',data=train_df)
#

def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train_df[train_df["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train_df["Age"] = train_df[["Age", "Pclass"]].apply(add_age,axis=1)
train_df.drop("Cabin",inplace=True,axis=1)
pd.get_dummies(train_df["Sex"])

sex = pd.get_dummies(train_df["Sex"],drop_first=True)
embarked = pd.get_dummies(train_df["Embarked"],drop_first=True)
pclass = pd.get_dummies(train_df["Pclass"],drop_first=True)


train_df = pd.concat([train_df,pclass,sex,embarked],axis=1)

train_df.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)

# print(train_df)

X = train_df.drop("Survived", axis=1)
y = train_df["Survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

# TODO: Predicting.
print("Prediction:\n")


def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(test_df[test_df["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

test_df["Age"] = test_df[["Age", "Pclass"]].apply(add_age,axis=1)
test_df.drop("Cabin",inplace=True,axis=1)
pd.get_dummies(test_df["Sex"])

sex = pd.get_dummies(test_df["Sex"],drop_first=True)
embarked = pd.get_dummies(test_df["Embarked"],drop_first=True)
pclass = pd.get_dummies(test_df["Pclass"],drop_first=True)


test_df = pd.concat([test_df,pclass,sex,embarked],axis=1)

test_df.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)
test_df.fillna(test_df["Fare"].mean(), inplace=True)

predictions = logmodel.predict(test_df)
print(pd.DataFrame(predictions, columns=['Survived']))

