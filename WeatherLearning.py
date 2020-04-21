import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

# output layer: linear regression

# for default arguments, python has them declared in the function call
def _init_(self, x, y, hidden_units = 10, learning_rate = 0.01, reg_lambda = 0):
    self.x = x
    self.y = y
    self.y_hat = np.zeros(y.shape)
    self.hidden_units = hidden_units
    # hidden units is just used in making the size of W1 and W2.
    # initialize with random weights
    self.W1 = np.random.randn(x.shape[1], hidden_units)
    # NEED TO FIGURE OUT HOW MANY OUTPUTS FOR THIS
    self.W2 = np.random.randn(hidden_units, 1)
    self.b1 = np.zeros((1 , hidden_units))
    self.b2 = np.zeros(1, 1)
    self.learning_rate = learning_rate
    self.epsilon = 1e-4
    self.reg_lambda = reg_lambda
    self.cost_history = []


def sigmoid(self, x):
    # activation function for the neurons
    return 1 / (1 +np.exp(-x))

def sigmoid_prime(self, x):
    # The derivative of the activation, used in backprob
    return x * (1 - x)

def feedforward(self):
    z1 = np.dot(self.x, self.W1) + self.b1
    self.a1 = self.sigmoid(z1)
    z2 = np.dot(self.a1, self.W2) + self.b2
    # MIGHT NEED TO CHANGE THIS LINE!!!!!
    # MIGHT NEED TO USE A LINEAR FUNCTION HERE
    self.y_hat = self.sigmoid(z2)

# In the example, this was only used to add to the cost history
def mean_squared_error_loss(self):
    regularization = self.reg_lambda * (np.sum(np.square(self.W1) + np.sum(np.square(self.W2))))
    loss = -np.mean(np.square(self.y - self.y_hat)) + regularization
    return loss

def backprop(self):
    delta_2 = self.y_hat - self.y
    dW2 = np.dot(self.a1.T, delta_2) + self.reg_lambda * self.W2

# function to load data from csv
def load_data(filename):
    return pd.read_csv(filename)


def processFlightData(data):
    return data.filter(
        ['Month', 'Day', 'Origin_Airport', 'WeatherDelay'])


# loading the weather data
weatherData = load_data("us-weather-events/US_WeatherEvents_2016-2019.csv")
# print()

# loading the 2015 flight data
# flight2015 = load_data('2015-flight-delays/flights.csv')

# loading the smaller 2017 flight data
flight2017 = load_data('flight-delays/fl_samp.csv')

flight2017Processed = processFlightData(flight2017)
print(flight2017Processed.head())
print(flight2017Processed["WeatherDelay"].max())

# loading the other flight data
flightData = load_data('flight-delays/flight.csv')

# flightDataWeatherDelay = flightData[flightData['WeatherDelay'] > 0]
# print(flightDataWeatherDelay.head())

flightDateProcessed = processFlightData(flightData)
print(flightDateProcessed.head())
