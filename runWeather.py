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
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("------------------Entering UI--------------")
print("enter exit into airport code to quit")
airportCode = "t"
while airportCode != 'exit':
    day = int(input("Enter the day of your flight(Ex. 1, 2, ..., 31): "))
    #print(type(day))
    month = int(input("Enter the month of your flight(Ex. 1, 2, ..., 12):"))
    if month > 12 | month < 1:
        print("invalid month")
        continue
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    airportCode = input("Enter the airportCode of your departure airport(Ex. KATL, KLAX, ..., KJFK). Enter exit to stop:")
    X_test = enc1.transform([[month, day, airportCode]]).toarray()
    y_pred = clf1.predict(X_test)
    if airportCode == 'exit':
        break
    if y_pred[0] == 0:
        print("isWeather calculated sunny weather for your flight on the", months[month-1], day, " at ", airportCode, "airport, assume no weather delay.")
        continue
    print("isWeather calculated the there to be ", y_pred[0], " on ", month, "/", day, " at ", airportCode, "airport.")
    X_test = enc2.transform([[month, day]]).toarray()
    y_pred = clf2.predict(X_test)
    print("isWeather calculated the there to be ", y_pred[0][0], " ", y_pred[0][1], " on ", month, "/", day, " at ", airportCode, "airport.")
    convertedAirport = changeCode.main(airportCode)
    if (convertedAirport == ""):
        print("Airport Code was not found in conversion table")
    else:
        X_test = enc3.transform([[month, day, convertedAirport]]).toarray()
        y_pred = clf3.predict(X_test)
        print("WeatherLearning calculated that there will be a ", y_pred, " delay")



