# weatherLearning
Blair Weaver and Coby Wissing

Github: <a href="https://github.com/cobywissing/weatherLearning">GitHub</a>

Datasets: <br>
[US Weather Events (2016 - 2019)](https://www.kaggle.com/sobhanmoosavi/us-weather-events) <br>
[flight delays](https://www.kaggle.com/mrferozi/flight-delays) <br>
[Airports, Train Stations, and Ferry Terminals](https://www.kaggle.com/open-flights/airports-train-stations-and-ferry-terminals) *modifed since no column headers and removed unneccessary data


To create the data sets run: <br>
- createWeather.sql<br>
- loadWeather.sql <br>
- exportdata.sql<br>
- insert the following line to TypeWeather.csv EventId	Type	Severity	AirportCode	month	day	year
- insert the following line to IsWeather.csv EventId	weather	AirportCode	month	day	year
- *be sure to have the alterted weather file from the drive

After this, run runWeather.py
