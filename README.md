# Twitter Geolocate
Twitter Geolocation is a webapp to generate twitter search querries for a certain geolocation and opens them in your standard webbrowser. Provide either GPS Coordinates or use the mapquest API to search for a location (requires a free account)

## Usage

As a python script this does not need to be installed but to run it you will require python 3.7 or higher and the following packages:

- requests
- json*
- webbrowser*

\* = should be provided with python3

## Provide coordinates

```
$ python3 geolocate.py -c <latitude> <longitude> <radius>
```

Example:
```
$ python3 geolocate.py -c 52.5186202 13.3761872 0.2km
```

## Search querry with mapquest

To use the mapquest api you will need an api key provided with a free account which will grant you 15000 requests per month (which are about 20 per hour if you use the service 24 hours per day)

You can read more here: https://developer.mapquest.com/documentation/

Once you have an api key you can use it to search for places.

```
$ python3 gelocate.py -q <key> <querry> <radius>
```

The program will then ask you to select one of the top 5 search results.

Example:
```
$ python3 geolocate.py -q myKEy "Platz der Republik 1, 11011 Berlin" 0.3km
Search Results:

(1) Käfer Dachgarten-Restaurant im Deutschen Bundestag, 1, Platz der Republik, Tiergarten, Mitte, Berlin, 11011, Deutschland
(2) Deutscher Bundestag, 1, Platz der Republik, Tiergarten, Mitte, Berlin, 11011, Deutschland

Please select an option or type "exit" to exit
>

```
