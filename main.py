import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, redirect)
import utils
import json
# Static Routes


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

# dynamic routes


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionData = [json.loads(utils.getJsonFromFile(show))
                   for show in utils.AVAILABE_SHOWS]
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/show/<show_id:int>/episode/<ep_id:int>')
def episode(show_id, ep_id):
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=utils.find_ep(show_id, ep_id))


@route('/ajax/show/<show_id>/episode/<ep_id:int>')
def episode_request(show_id, ep_id):
    return template("./templates/episode.tpl",  result=utils.find_ep(show_id, ep_id))


@route('/show/<show_id:int>')
def show(show_id):
    sectionData = json.loads(utils.getJsonFromFile(show_id))
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/ajax/show/<show_id>')
def show_request(show_id):
    sectionData = json.loads(utils.getJsonFromFile(show_id))
    return template("./templates/show.tpl",  result=sectionData)


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@post('/search')
def search_result():
    sectionTemplate = "./templates/search_result.tpl"
    query = request.forms.get('q')
    results = utils.get_results(query)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=results, query=query)


run(host='localhost', port=os.environ.get(
    'PORT', 5000), reloader=True, debug=True)
