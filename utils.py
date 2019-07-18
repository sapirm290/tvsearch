from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143",
                  "175", "216", "1371", "1871", "2993", "305"]


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def find_ep(show_id, ep_id):
    for ep in json.loads(getJsonFromFile(show_id))['_embedded']['episodes']:
        if ep['id'] == ep_id:
            return ep
    return None


def find_show(show_id):
    return json.loads(getJsonFromFile(show_id))
