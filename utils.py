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

    query = query.lower()
    results = []
    for show in AVAILABE_SHOWS:
        show_as_dict = json.loads(getJsonFromFile(show))
        if(query in show_as_dict['name'].lower()):
            results.append({
                'showid': show_as_dict['id'],
                'text': show_as_dict['name']
            })
        for episode in show_as_dict['_embedded']['episodes']:
            try:
                if (query in episode['name'].lower()) or (query in episode['summary'].lower()):
                    results.append({
                        'showid': show_as_dict['id'],
                        'episodeid': episode['id'],
                        'text': ':'.join([show_as_dict['name'], episode['name']])
                    })
            except:
                pass

    def is_episode_or_show(result):
        if 'episodeid' in result:
            return True
        return False
    return sorted(results, key=is_episode_or_show)


def find_show(show_id):
    return json.loads(getJsonFromFile(show_id))
