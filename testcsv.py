import pydotplus
import graphviz
import collections
import csv as c
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import os
#the below line had to be added due to issues with graphviz conda files see the following link: https://datascience.stackexchange.com/questions/37428/graphviz-not-working-when-imported-inside-pydotplus-graphvizs-executables-not
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
#C:\Users\cobyw\Desktop\homework\machine learning\dataset.csv
enc = OneHotEncoder(handle_unknown='ignore')
#with open('dataset.csv', newline='') as csvfile:
#    spamreader = c.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(' '.join(row))
df = pd.read_csv(r"C:\Users\cobyw\Desktop\homework\machine learning\IsWeather.csv")
lb = preprocessing.LabelEncoder()
lf = preprocessing.LabelEncoder()
#y_one_hot_encoder = LabelBinarizer()
print(df.shape)
#print(train_dataset.head())
#print(test_dataset.shape)
X_columns = ['AirportCode','month','day', 'year']
y_column = ['weather']

X_data = df[X_columns].to_numpy()
y_data = df[y_column].to_numpy()
X_data = X_data.tolist()
y_data = y_data.tolist()
print(X_data[0])
print(y_data[0])


X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
#lb.fit(X_train)
#lf.fit(y_data)
#lb.transform(X_train)
#lf.transform(y_data)

enc.fit(X_data)
print("transforming X's dataset on : ", enc.categories_, "\n")
X_train = enc.transform(X_train).toarray()
X_test = enc.transform(X_test).toarray()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#dot_data = tree.export_graphviz(clf,
#                                feature_names=data_feature_names,
#                                out_file=None,
#                                filled=True,
#                                rounded=True)
#graph = pydotplus.graph_from_dot_data(dot_data)
#colors = ('turquoise', 'orange')
#edges = collections.defaultdict(list)

#for edge in graph.get_edge_list():
#    edges[edge.get_source()].append(int(edge.get_destination()))

#for edge in edges:
#    edges[edge].sort()    
#    for i in range(2):
#        dest = graph.get_node(str(edges[edge][i]))[0]
#        dest.set_fillcolor(colors[i])


#graph.write_pdf(r'C:\Users\cobyw\Desktop\homework\machine learning\tree.pdf')
