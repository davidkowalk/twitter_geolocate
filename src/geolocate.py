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

To search using a 3-word address:
$ python3 -w <key> <querry> <radius>
"""

def main():

    if len(args) == 5 and args[1] == "-c":
        lat = args[2]
        lon = args[3]
        rad = args[4]

        url = twitter.get_url(lat, lon, rad)
        twitter.open_standard_browser(url)


    elif 4 <= len(args) <= 5 and args[1] == "-q":
        import mapquest

        i = 2

        if len(args) == 5:
            key = args[i]
            i += 1
        elif len(args) == 4:
            from os.path import exists

            if exists("./mapkey.txt"):

                with open("./mapkey.txt", "r") as f:
                    key = f.read().split("\n")[0]

            else:
                print("Could not find key.txt. Please provide a key in the command or create the file \"mapkey.txt\" in the current working directory.\nUse \"python3 geolocation.py\" for help.")
                exit(2)

        querry = args[i]
        i += 1

        radius = args[i]

        full_response, code = mapquest.get_json(key, querry)

        if code != 200:
            print("An error has occured!\n{msg}".format(msg=full_response))
            exit(3)

        lat, lon = mapquest.choose_option(full_response)

        url = twitter.get_url(lat, lon, radius)
        twitter.open_standard_browser(url)

    elif 4 <= len(args) <= 5 and args[1] == "-w":
        import what_three_words as words

        i = 2

        if len(args) == 5:
            key = args[i]
            i += 1
        elif len(args) == 4:
            from os.path import exists

            if exists("./wordkey.txt"):

                with open("./wordkey.txt", "r") as f:
                    key = f.read().split("\n")[0]

            else:
                print("Could not find key.txt. Please provide a key in the command or create the file \"wordkey.txt\" in the current working directory.\nUse \"python3 geolocation.py\" for help.")
                exit(2)


        querry = words.clean_querry(args[i])
        i += 1

        radius = args[i]

        full_response, code = words.get_json(key, querry)

        if code != 200:
            print("An error has occured!\n{msg}".format(msg=full_response))
            exit(3)

        lat = full_response["square"]["southwest"]["lat"]
        lon = full_response["square"]["southwest"]["lng"]

        url = twitter.get_url(lat, lon, radius)
        twitter.open_standard_browser(url)

    else:
        print(help_str)

if __name__ == '__main__':
    main()
