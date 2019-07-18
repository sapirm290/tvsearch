import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, redirect, error)
from utils import getVersion, getJsonFromFile, find_ep, find_show, AVAILABE_SHOWS
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
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionData = [json.loads(getJsonFromFile(show))
                   for show in AVAILABE_SHOWS]
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/show/<show_id:int>/episode/<ep_id:int>')
def episode(show_id, ep_id):
    section_data = find_ep(show_id, ep_id)
    if(section_data == None):
        redirect('/error')    
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData=section_data)


@route('/ajax/show/<show_id>/episode/<ep_id:int>')
def episode_request(show_id, ep_id):
    section_data = find_ep(show_id, ep_id)
    if(section_data ==None):
        redirect('/error')
    return template("./templates/episode.tpl",  result=section_data)


@route('/show/<show_id:int>')
def show(show_id):
    sectionTemplate = "./templates/show.tpl"
    section_data = find_show(show_id)
    if(section_data == {}):
        redirect('/error')
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData=section_data)


@route('/ajax/show/<show_id>')
def show_request(show_id):
    section_data = find_show(show_id)
    if(section_data == {}):
        redirect('/error')
    return template("./templates/show.tpl",  result=section_data)


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@post('/search')
def search_result():
    sectionTemplate = "./templates/search_result.tpl"
    query = request.forms.get('q')
    results = utils.get_results(query)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=results, query=query)


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=getVersion(), sectionTemplate=sectionTemplate, sectionData={})


run(host='localhost', port=os.environ.get(
    'PORT', 5000), reloader=True, debug=True)
