import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

train_df = pd.read_csv("train_new.csv")
test_df = pd.read_csv("test_new.csv")

# TODO: Identify columns having NULL values
# print(train_df.isnull().sum())
# sns.heatmap(train_df.isnull())
# plt.show()

# TODO: Identifying that LoanAmount and Loan_Amount_Term have what kind of mean in different categories .
# sns.boxenplot(x="Gender", y="LoanAmount", data=train_df)
# sns.boxenplot(x="Education", y="LoanAmount", data=train_df)
# sns.boxenplot(x="Gender", y="Loan_Amount_Term", data=train_df)
# sns.boxenplot(x="Education", y="Loan_Amount_Term", data=train_df)
# plt.show()

# TODO: Check whether independent are correlated or not.
# sns.lmplot(x='LoanAmount', y='Loan_Amount_Term', data=train_df)
# sns.lmplot(x='ApplicantIncome', y='CoapplicantIncome', data=train_df)
# plt.show()


def add_la(cols):
    temp = cols[0]
    if pd.isnull(temp):
        return int(train_df["LoanAmount"].mean())
    else:
        return temp


def add_lat(cols):
    temp = cols[0]
    if pd.isnull(temp):
        return int(train_df["Loan_Amount_Term"].mean())
    else:
        return temp


# TODO: Filling NULL values in LoanAmount and Loan_Amount_Term columns.
train_df["LoanAmount"] = train_df[["LoanAmount"]].apply(add_la, axis=1)
train_df["Loan_Amount_Term"] = train_df[['Loan_Amount_Term']].apply(add_la, axis=1)

# TODO : Remove rows having any NULL value.
train_df.dropna(inplace=True)


gender = pd.get_dummies(train_df['Gender'], drop_first=True)
married = pd.get_dummies(train_df['Married'], drop_first=True)
dependents = pd.get_dummies(train_df['Dependents'], drop_first=True)
education = pd.get_dummies(train_df['Education'], drop_first=True)
self_employed = pd.get_dummies(train_df['Self_Employed'], drop_first=True)
credit_history = pd.get_dummies(train_df['Credit_History'], drop_first=True)
Property = pd.get_dummies(train_df['Property_Area'], drop_first=True)
loan_status = pd.get_dummies(train_df['Loan_Status'], drop_first=True)

train_df = pd.concat([train_df, gender, married, dependents, education, self_employed, credit_history, Property, loan_status], axis=1)

# print(train_df)

train_df.drop(["Loan_ID", "Gender", "Married", "Dependents", "Education", "Self_Employed", "Credit_History", "Property_Area", "Loan_Status"], axis=1, inplace=True)

print(train_df)

x = train_df.drop(["Y", "CoapplicantIncome", "ApplicantIncome", "Urban", "Semiurban", "Male"], axis=1)
y = train_df["Y"]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=16)

from sklearn.linear_model import LogisticRegression
obj = LogisticRegression()

obj.fit(x_train, y_train)

y_predict = obj.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print("Accuracy: ", accuracy_score(y_test, y_predict))
print(classification_report(y_test, y_predict))
print(confusion_matrix(y_test, y_predict))

# TODO: Predictions over test_df

test_df["LoanAmount"] = test_df["LoanAmount"].fillna(test_df["LoanAmount"].mean())
test_df["Loan_Amount_Term"] = test_df["Loan_Amount_Term"].fillna(test_df["Loan_Amount_Term"].mean())

train_df.dropna(inplace=True)

gender = pd.get_dummies(test_df['Gender'], drop_first=True)
married = pd.get_dummies(test_df['Married'], drop_first=True)
dependents = pd.get_dummies(test_df['Dependents'], drop_first=True)
education = pd.get_dummies(test_df['Education'], drop_first=True)
self_employed = pd.get_dummies(test_df['Self_Employed'], drop_first=True)
credit_history = pd.get_dummies(test_df['Credit_History'], drop_first=True)
Property = pd.get_dummies(test_df['Property_Area'], drop_first=True)

test_df = pd.concat([test_df, gender, married, dependents, education, self_employed, credit_history, Property], axis=1)
test_df.drop(["Loan_ID", "Gender", "Married", "Dependents", "Education", "Self_Employed", "Credit_History", "Property_Area"], axis=1, inplace=True)
x = test_df.drop(["CoapplicantIncome", "ApplicantIncome", "Urban", "Semiurban", "Male"], axis=1)

y = pd.DataFrame(obj.predict(x), columns=["Loan_Status"])
y.loc[y["Loan_Status"] == 1] = "Y"
y.loc[y["Loan_Status"] == 0] = "N"
print(y)

temp = np.arange()
