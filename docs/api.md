# API

This document explains the separate modules of the application.

## geolocate

The `geolocate.py` functions as the main application file. In computes the console arguments and contains the `main()` function.

## mapquest

The `mapquest.py` file interfaces with the mapquest api. It downloads and processes the map data.

### get_json()

**Arguments:** string key, string querry

**Output:** dict | string result, int status_code

This will querry the mapquest-api with a location (querry) and return the entire json as a dictionary if successfull, or as a string if not successfull along with the http-status-code.

**Example:**
```python
result, status = mapquest.get_json(myKey, querry)
```

### choose_option()

**Arguments:** dict full_json

**Output:** float latitude, float longitude

Takes the dictionary from the mapquest-api and generates a user interface to select the desired location. If only one option is available it will be autoselected.
The function then extracts the coordinates from the selected location.

**Example:**
```python
result, status = mapquest.get_json(myKey, querry)
if status == 200:
  lat, long = mapquest.choose_option(result)
```

## twitter

The `twitter.py` generates the twitter search querry and opens the standard browser.

### get_url()

**Arguments:** latitude, longitude, radius

**Output:** string url

Formats the twitter search-url with latitude, longitude and radius

**Example:**
```python
lat, long = 52.5186202, 13.3761872
radius = "0.2km"

url = twitter.get_url(lat, long, radius)
```

### open_standard_browser()

**Arguments:** string url

Opens the standard webbrowser of your operating system.
