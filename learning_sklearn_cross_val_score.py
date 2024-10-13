from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
X = boston["data"]
y = boston["target"]
lr = LinearRegression()
kf = KFold(n_splits=5) 
neg_mses = cross_val_score(lr, X, y, cv=kf, scoring='neg_mean_squared_error')
mses = [-i for i in neg_mses]

print('MSES:')
print(mses)
print('\nAverage MSE:')
print(sum(mses) / len(mses))