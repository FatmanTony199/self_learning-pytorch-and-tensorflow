import pandas as pd

titanic_url = "https://kaggle-getting-started.s3-ap-northeast-1.amazonaws.com/titanic/train.csv"
titanic_df = pd.read_csv(titanic_url)
titanic_df.head()

y = titanic_df[['Survived']].values.reshape(-1, 1)
print(y)

X = titanic_df.drop('Survived', axis = 1).values
print(X)