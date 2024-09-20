#python learning_pandas.py
import pandas as pd
s = pd.Series([1, 2, 3, 4])
print(s)

num = {"1":"王","2":"王","3":"王","4":"王","5":"王",
"6":"王","7":"王","8":"王","9":"王","10":"王",
"21":"王","22":"王","23":"王","24":"王","25":"王",
"26":"王","27":"王","28":"王","29":"王","30":"王" }
num = pd.Series(num)
print(num)

clas = {'name':['Tony', 'jerry', 'gary', 'hom', 'mark'],
		'number':['20', '24', '13', '7', '16'],}
print(pd.DataFrame(clas))

print(pd.DataFrame(clas).head(3))
find = pd.DataFrame(clas, columns = ['number', 'name'])
print(find)
print(find['name'])
