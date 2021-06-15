"""
https://api.what3words.com/v3/convert-to-coordinates?words=filled.count.soap&key=[API-KEY]
"""

import json, requests

def get_json(key, querry):

    querry = querry.replace(" ", "+")
    limit = 5
    url = "https://api.what3words.com/v3/convert-to-coordinates?words={querry}&key={key}"

    r = requests.get(url.format(key=key, querry=querry, limit = limit))
    if r.status_code == 200:
        result = json.loads(r.text)
    else:
        result = r.text
    return result, r.status_code
