import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
def main():
    
    df = pd.read_csv(r"IsWeather.csv")
    #y_one_hot_encoder = LabelBinarizer()
    #print(df.shape)
    #print(df.head())
    #print(test_dataset.shape)
    X_columns = ['month','day']#'AirportCode'
    y_column = ['weather']

    X_data = df[X_columns].to_numpy()
    y_data = df[y_column].to_numpy()
    X_data = X_data.tolist()
    y_data = y_data.tolist()
    #print(X_data[0])
    #print(y_data[0])


    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)

    enc.fit(X_data)
    #print("transforming X's dataset on : ", enc.categories_, "\n")
    X_train = enc.transform(X_train).toarray()
    X_test = enc.transform(X_test).toarray()

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    return clf
def getEncoder():
    return enc
