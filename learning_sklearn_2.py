import pandas as pd
from sklearn.model_selection import train_test_split

housing_train = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")

X = housing_train.drop('SalePrice', axis = 1)
X_train, X_validation = train_test_split(X, test_size = 0.33, random_state = 42)

print('Before Splitting:')
print(X.shape)

print('After Splitting:')
print(X_train.shape, X_validation.shape)