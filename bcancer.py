import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: read cvs
df = pd.read_csv("data.csv")
print(df.head())

# TODO: count null values
print(df.isnull().sum())
df.dropna(axis=1, inplace=True)

df['diagnosis'] = df['diagnosis'].map({'M': 0, "B": 1})
print(df.head())

# TODO: Analysis
# sns.countplot(x='diagnosis', data=df)
# plt.show()

x = df[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
       'symmetry_mean', 'fractal_dimension_mean']]
y = df['diagnosis']

# TODO: KNN Algorithm
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = pd.DataFrame(ss.fit_transform(x), columns=x.columns)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=7)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)

print("Using KNN:-")
from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_predict))
print("Accuracy score:", accuracy_score(y_test, y_predict))

# TODO: Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)

print("Using Logistic Regression:-")
print(confusion_matrix(y_test, y_predict))
print("Accuracy score:", accuracy_score(y_test, y_predict))

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
y_predict = dt.predict(x_test)

print("Using Decision tree:-")
print(confusion_matrix(y_test, y_predict))
print("Accuracy score:", accuracy_score(y_test, y_predict))


