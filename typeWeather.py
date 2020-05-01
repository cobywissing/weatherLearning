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
enc = OneHotEncoder(handle_unknown='ignore')
def main():
    
    df = pd.read_csv(r"TypeWeather.csv")
    lb = preprocessing.LabelEncoder()
    lf = preprocessing.LabelEncoder()
    #y_one_hot_encoder = LabelBinarizer()
    #print(df.shape)
    #print(train_dataset.head())
    #print(test_dataset.shape)
    X_columns = ['AirportCode', 'month','day', 'year', 'AirportCode']#'AirportCode',
    y_column = ['Type', 'Severity']

    X_data = df[X_columns].to_numpy()
    y_data = df[y_column].to_numpy()
    X_data = X_data.tolist()
    y_data = y_data.tolist()
    #print(X_data[0])
    #print(y_data[0])


    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
    #lb.fit(X_train)
    #lf.fit(y_data)
    #lb.transform(X_train)
    #lf.transform(y_data)

    enc.fit(X_data)
    #print("transforming X's dataset on : ", enc.categories_, "\n")
    X_train = enc.transform(X_train).toarray()
    X_test = enc.transform(X_test).toarray()

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    y_pred = y_pred.tolist()
    #print(type(y_pred[0]))
    #print(type(y_test[0]))
    #print(len(y_pred))
    #print(len(y_test))
    #print(y_pred[0])
    #print(y_test[0])
    #print(type(y_pred[0]))
    #print(type(y_test[0]))
    count = 0
    count2 = 0
    count3 = 0
    #count4 = 0
    #flag = 0
    for i in range(len(y_pred)):
        #flag = 0
        if y_pred[i] == y_test[i]:
            count += 1
        if y_pred[i] == y_test[i][0]:
            count2 += 1
        #    flag =+ 1
        if y_pred[i][1] == y_test[i][1]:
            count3 += 1
        #    flag =+ 1
        #if flag > 0:
        #    count4 += 1
    count = count / len(y_pred)
    count2 = count2 / len(y_pred)
    count3 = count3 / len(y_pred)
    #count4 = count4 / len(y_pred)
    #print(len(y_pred))
    print("weather and severity accuracy: ", count)
    print("weather type accuracy: ", count2)
    print("severity type accuracy: ", count3)
    #print("weather or severity accuracy: ", count4)
    return clf
def getEncoder():
    return enc
