import pandas as pd

housing = pd.read_csv('https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = housing['GrLivArea'].values.reshape(-1, 1)
y = housing['SalePrice'].values.reshape(-1 ,1 )
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.33, random_state = 42)

lr = LinearRegression()
lr.fit(X_train, y_train)

print('Intercept:')
print(lr.intercept_)

print('Coefficient:')
print(lr.coef_)


y_pred = lr.predict(X_validation)

print('真實數字:')
print(y_validation[:5])

print('\n')
print('預測結果:')
print(y_pred[:5])