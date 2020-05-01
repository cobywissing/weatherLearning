import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer



# function to load data from csv
def load_data(filename):
    return pd.read_csv(filename)


def processFlightData(data):
    return data.filter(
        ['Month', 'Day', 'Origin_Airport', 'WeatherDelay']) #


def main():
        # loading the smaller 2017 flight data
    flight2017 = load_data('flight-delays/fl_samp.csv')
    flight2017Processed = processFlightData(flight2017)

    # loading the other flight data
    flightData = load_data('flight-delays/flight.csv')
    flightDateProcessed = processFlightData(flightData)

    # Combine the two datasets
    frames = [flight2017Processed, flightDateProcessed]
    combinedFlightData = pd.concat(frames)

    print(combinedFlightData.loc[:, "Origin_Airport"].value_counts())

    # preprossess data
    # Establish variables
    scalar = StandardScaler()
    ct = ColumnTransformer(
        [("onehot", OneHotEncoder(sparse=False), ["Month", "Day", "Origin_Airport"])]
    )

    # Set the X and Y for the datasets
    X = combinedFlightData.loc[:, "Month":"Origin_Airport"] #
    y = combinedFlightData["WeatherDelay"].values

    ct.fit(X)
    X_trans = ct.transform(X)

    # Split the dataset into Test, Train, and Validate
    X_train_full, x_test, Y_train_full, y_test = train_test_split(X_trans, y, test_size=0.2)
    X_train, X_valid, Y_train, Y_valid = train_test_split(X_train_full, Y_train_full, test_size=0.2)

    # Set up model
    model = keras.models.Sequential([
        keras.layers.Dense(500, activation="relu", input_shape=X_train.shape[1:]),
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(50, activation="relu"),
        keras.layers.Dense(1)
    ])
    model.compile(loss="mean_squared_error", optimizer="adam", metrics=["mean_squared_error", "accuracy"])

    #train
    history = model.fit(X_train, Y_train, epochs=100,
                        validation_data=(X_valid, Y_valid))

    # evaluate
    model_test = model.evaluate(x_test, y_test)

    # Plot results
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.show()