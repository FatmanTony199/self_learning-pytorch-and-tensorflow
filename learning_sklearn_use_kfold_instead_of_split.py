from sklearn.model_selection import KFold
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

boston = load_boston()
X = boston["data"]
y = boston["target"]
kf = KFold(n_splits=5)
mses = []
for train_indices, validation_indices in kf.split(X):
    X_train, X_validation, y_train, y_validation = X[train_indices, :], X[validation_indices, :], y[train_indices], y[validation_indices]
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_validation)
    mses.append(mean_squared_error(y_validation, y_pred))
print(mses)
print(sum(mses) / len(mses))