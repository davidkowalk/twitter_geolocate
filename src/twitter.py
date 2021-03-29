import webbrowser as browser

def get_url(lat, lon, radius):
    url = "https://twitter.com/search?q=geocode:{lat},{lon},{radius}"
    return url.format(lat=lat, lon=lon, radius=radius)

def open_standard_browser(url):
    browser.open(url)
