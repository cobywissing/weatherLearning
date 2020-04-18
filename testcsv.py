import pydotplus
import graphviz
import collections
import csv as c
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder
import os
#the below line had to be added due to issues with graphviz conda files see the following link: https://datascience.stackexchange.com/questions/37428/graphviz-not-working-when-imported-inside-pydotplus-graphvizs-executables-not
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
#C:\Users\cobyw\Desktop\homework\machine learning\dataset.csv
enc = OneHotEncoder(handle_unknown='ignore')
with open('dataset.csv', newline='') as csvfile:
    spamreader = c.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(' '.join(row))
train_dataset = pd.read_csv(r"C:\Users\cobyw\Desktop\homework\machine learning\US_WeatherEvents_2016-2019Alterded.csv")

print(train_dataset.shape)
#print(train_dataset.head())
#print(test_dataset.shape)
X = train_dataset.drop(['EventId','Type','Severity','StartTime(UTC)','EndTime(UTC)'], axis=1)
Y = train_dataset['AirportCode']

X_data = df[X_columns].to_numpy()
y_data = df[y_column].to_numpy().reshape((-1, 1))
X_data = X_one_hot_encoder.fit_transform(X_data)
y_data = y_one_hot_encoder.fit_transform(y_data).ravel()
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Projected Y_test values \n", y_pred, "\n")
print("Actual Y_test values:\n",y_test, "\n")
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
