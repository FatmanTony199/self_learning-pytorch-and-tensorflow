from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston = load_boston()
X = boston['data']
y = boston['target']

X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.33, random_state = 42)

print('X_train\'s shape:')
print(X_train.shape)

print('X_validation\'s shape:')
print(X_validation.shape)

print('y_train\'s shape:')
print(y_train.shape)

print('y_validation\'s shape:')
print(y_validation.shape)