import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def main(value):
    airportCodes = load_data("airports-extended.csv")
    codeLocation = airportCodes.loc[airportCodes['ICAO'] == value]
    if (not len(codeLocation) == 0):
        covertedCode = codeLocation.index[0]
        return airportCodes.iloc[covertedCode, 0]
    else:
        return ""