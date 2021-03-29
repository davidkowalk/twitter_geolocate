from sys import argv as args
import twitter

help_str = """
Twitter Geolocate let's you search twitter for tweets in a certain area.

<> Required
[] Optional

To search for coordinates:
$ python3 -c <latitude> <longitude> <radius>

To search for a location name using mapquest-api:
$ python3 -q <key> <querry> <radius>
"""

def main():

    if len(args) == 5 and args[1] == "-c":
        lat = args[2]
        lon = args[3]
        rad = args[4]

        url = twitter.get_url(lat, lon, rad)
        twitter.open_standard_browser(url)
    elif len(args) == 5 and args[1] == "-q":

        import mapquest

        key = args[2]
        querry = args[3]
        radius = args[4]

        full_repsonse, code = mapquest.get_json(key, querry)

        if code != 200:
            print("An error has occured!\n{msg}".format(msg=full_repsonse))

        lat, lon = mapquest.choose_option(full_repsonse)

        url = twitter.get_url(lat, lon, radius)
        twitter.open_standard_browser(url)

    else:
        print(help_str)

if __name__ == '__main__':
    main()
