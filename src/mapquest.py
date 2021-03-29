import json, requests

def get_json(querry, key):

    url = "http://open.mapquestapi.com/nominatim/v1/search.php?key={key}&format=json&q={querry}&addressdetails=0&limit=3"

    r = requests.get(url)
    return json.loads(r.text), r.status_code
