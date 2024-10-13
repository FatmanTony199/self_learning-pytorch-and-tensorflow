from sklearn.model_selection import KFold

kf = KFold(n_splits=5)
housing_train = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
X = housing_train.drop("SalePrice", axis=1)
for train_indices, validation_indices in kf.split(X):
    print(train_indices, validation_indices)