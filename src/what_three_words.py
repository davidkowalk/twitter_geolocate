import json, requests

def get_json(key: str, querry: str):

    querry = querry.replace(" ", "+")
    limit = 5
    url = "https://api.what3words.com/v3/convert-to-coordinates?words={querry}&key={key}"

    r = requests.get(url.format(key=key, querry=querry, limit = limit))
    if r.status_code == 200:
        result = json.loads(r.text)
    else:
        result = r.text
    return result, r.status_code

def clean_querry(querry: str):
    """
    Will remove the 3 slashes from the beginning of a querry
    """

    if len(querry) > 3 and querry[:3] == "///":
        return querry[3:]
    else:
        return querry
