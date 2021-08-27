import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("BostonHousing.csv")

#sns.heatmap(df.corr(), annot=True)
#plt.show()

y = df["medv"]
x = df[["rm", "ptratio", "lstat"]]

#sns.distplot(df["medv"])
#sns.pairplot(df[:2])

#sns.lmplot(x="medv", y="rm", data=df)
#sns.lmplot(x="medv", y="ptratio", data=df)
#sns.lmplot(x="medv", y="lstat", data=df)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=15)

from sklearn.linear_model import LinearRegression
obj = LinearRegression()

obj.fit(x_train, y_train)
#print(obj.intercept_)

y_predict = obj.predict(x_test)
#plt.scatter(y_predict, y_test)

#plt.show()
sc = obj.score(x_test, y_test)
print(sc)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print(mean_absolute_error(y_test, y_predict))
print(mean_squared_error(y_test, y_predict))
print(r2_score(y_test, y_predict))
