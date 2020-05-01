import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)
def main():
    temp = load_data("airports-extended.csv")

    print(temp.head())
    value = 'ATL'


    # temp.c1[temp.c1 == 8].index.tolist()
temp = load_data("airports-extended.csv")

print(temp.head())
value = 'KATL'


temp1 = temp.loc[temp['ICAO'] == value].index[0]
print(temp1)
print(temp.iloc[temp1, 0])