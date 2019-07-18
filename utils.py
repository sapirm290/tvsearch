import bottle
import json
from bottle import template

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


def get_results(query):
    results = []
    for s in AVAILABE_SHOWS:
        text = getJsonFromFile(s)
        in_episodes = text.find('_embedded')
        if (text.lower().find(query.lower()) == -1):
            print('not here')
        elif (text.lower().find(query.lower()) < in_episodes):
            results.append({'showid': s, 'text': json.loads(
                text)['summary']})
            print(f"series: {json.loads(text)['name']}")
        else:
            for ep in json.loads(text)['_embedded']['episodes']:
                if str(ep['summary']).lower().find(query.lower()) != -1:
                    print(
                        f"episode id: {ep['id']} in series: {json.loads(text)['name']}")
                    results.append({'showid': s, 'episodeid': ep['id'], 'text':
                                    ep['summary']})
    return results


get_results('stranger')
def find_show(show_id):
    return json.loads(getJsonFromFile(show_id))
