import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
x = random.sample(range(0, 1000), 200)
y = random.sample(range(0, 1000), 200)
z = [x[i] + y[i] for i in range(200)]

df = pd.DataFrame({"X": x, "Y": y, "Z": z})
print(df.head())
x = df[["X", "Y"]]
y = df['Z']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=3)

from sklearn.linear_model import LinearRegression
obj = LinearRegression()

obj.fit(x_train, y_train)
print("Accuracy: ", obj.score(x_test, y_test))

y_predict = obj.predict(x_test)
sns.scatterplot(y_test, y_predict)
plt.show()
