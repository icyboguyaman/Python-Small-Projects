import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the data sets.
pd.set_option('display.max_rows', None)
df_train = pd.read_csv("house-prices-train.csv")
df_test = pd.read_csv("house-prices-test.csv")

# TODO: display data set.
print(df_train.head())
print("Rows : ", len(df_train))
print("Column: ", len(df_train.columns))
print("Column names : ", df_train.columns)

# TODO: Examine NULL count adn removing NULL values.
print(df_train.isnull().sum())
df_train.drop(["Alley", "PoolQC", "Fence", "MiscFeature"], axis=1, inplace=True)

pd.set_option('display.max_column', None)
print(df_train.corr()['LotFrontage'])
print(df_train.corr()['BsmtQual'])
