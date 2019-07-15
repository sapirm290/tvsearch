import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils

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
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/show')
def show():
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/episode')
def episode():
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search_result')
def search_result():
    sectionTemplate = "./templates/search_result.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})



run(host='0.0.0.0', port=os.environ.get('PORT', 5000), reloader=True)
