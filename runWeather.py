import typeWeather
import isWeather
import WeatherLearning

print("Preparing isWeather.py")
clf1 = isWeather.main()
enc1 = isWeather.getEncoder()
print("------------------DONE--------------")
print("Preparing typeWeather.py")
clf2 = typeWeather.main()
enc2 = typeWeather.getEncoder()
print("------------------DONE--------------")
print("Preparing WeatherLearning.py")
clf3 = WeatherLearning.main()
enc3 = WeatherLearning.getEncoder()
print("------------------DONE--------------")