import json, requests

def get_json(key, querry):

    querry = querry.replace(" ", "+")
    limit = 5
    url = "http://open.mapquestapi.com/nominatim/v1/search.php?key={key}&format=json&q={querry}&addressdetails=0&limit={limit}"

    r = requests.get(url.format(key=key, querry=querry, limit = limit))
    if r.status_code == 200:
        result = json.loads(r.text)
    else:
        result = r.text
    return result, r.status_code

def choose_option(full_json):
    """
    Takes full json-api-response and returns latitude and longitude as strings
    """

    print("Search Results:\n")

    i = 1

    for result in full_json:
        print(f"({i}) {result['display_name']}")
        i += 1

    success = False
    print("\nPlease select an option or type \"exit\" to exit")

    while not success:
        c = input(">")

        if c == "exit":
            exit(5)

        try:
            selection = int(c)
            success = True
        except:
            print(f"Could not find result No. {c}\n")

    return full_json[selection-1]["lat"], full_json[selection-1]["lon"]
