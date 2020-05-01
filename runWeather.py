import typeWeather
import isWeather
import WeatherLearning
import changeCode

print("--------------Preparing isWeather.py--------------")
clf1 = isWeather.main()
enc1 = isWeather.getEncoder()
print("------------------DONE--------------")
print("--------------Preparing typeWeather.py-------------")
clf2 = typeWeather.main()
enc2 = typeWeather.getEncoder()
print("------------------DONE--------------")
print("--------------Preparing WeatherLearning.py---------------")
clf3 = WeatherLearning.main()
enc3 = WeatherLearning.getEncoder()
print("------------------DONE--------------")

month = input("Enter a month (1-12):" )
day = input("Enter a day (1-31):")
airport = input("Enter an airport code (ex. KATL):")

convertedAirport = changeCode.main(airport)
if(convertedAirport == ""):
    print("Airport Code was not found in conversion table")
else:
    pass