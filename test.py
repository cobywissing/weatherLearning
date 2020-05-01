import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

temp = load_data("airports-extended.csv")

print(temp.head())
value = 'ATL'
listOfPos = list()
# Get bool dataframe with True at positions where the given value exists
result = temp.isin([value])
# Get list of columns that contains the value
seriesObj = result.any()
columnNames = list(seriesObj[seriesObj == True].index)
# Iterate over list of columns and fetch the rows indexes where value exists
for col in columnNames:
    rows = list(result[col][result[col] == True].index)
    for row in rows:
        listOfPos.append((row, col))

print(listOfPos)

