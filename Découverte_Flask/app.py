#!/usr/bin/env python3
# coding: utf-8

from flask import Flask
from flask import abort, request, make_response
from flask import render_template, redirect, url_for

from data import USERS
# Set API dev in an another file
from api import SITE_API


HELLO_STRINGS = {
        "cn": "你好世界\n",
        "du": "Hallo wereld\n",
        "en": "Hello world\n",
        "fr": "Bonjour monde\n",
        "de": "Hallo Welt\n",
        "gr": "γειά σου κόσμος\n",
        "it": "Ciao mondo\n",
        "jp": "こんにちは世界\n",
        "kr": "여보세요 세계\n",
        "pt": "Olá mundo\n",
        "ru": "Здравствуй, мир\n",
        "sp": "Hola mundo\n"
}
app = Flask(__name__)
# Add the API
app.register_blueprint(SITE_API)


@app.route('/hello_world')
def hello_world():
    app.logger.debug('Hello world')
    app.logger.debug('Here is the request I got: {}'.format(request))
    app.logger.debug('Here is the headers I got: {}'.format([k for k in request.headers.keys()]))
    req=request.headers
    if "Accept-Language" in req:
        if req["Accept-Language"] in HELLO_STRINGS:
            response = make_response(HELLO_STRINGS[req["Accept-Language"]])
            response.headers['Content-Language'] = req["Accept-Language"]
        else: #riendutout
            response = make_response(HELLO_STRINGS["en"])
            response.headers['Content-Language'] = "en"
    else:
        response = make_response(HELLO_STRINGS["en"])
        response.headers['Content-Language'] = "en"
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    
    response.headers['strength'] = '18'
    return response


@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('index.html')

@app.route('/flask')
def flaskintro():
    app.logger.debug('serving root URL /')
    return render_template('flask.html')


@app.route('/indexapi')
def indexapi():
    return render_template('indexapi.html')


@app.route('/about')
def about():
    from datetime import datetime
    today = datetime.today()
    app.logger.debug('about')
    return render_template('about.html', date=today,page_title="new title")


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/users', methods=['GET','POST'])
@app.route('/users/<username>/')
def users(username=None):
    if not username:
      if request.method == 'POST':
        app.logger.debug(request.form)
        USERS.append(request.form)
        return render_template('users.html',users=[USERS[i]["name"] for i in range(len(USERS))])
      else:
        return render_template('users.html',users=[USERS[i]["name"] for i in range(len(USERS))])
    elif username in [USERS[i]["name"] for i in range(len(USERS))]:
        index = [USERS[i]["name"] for i in range(len(USERS))].index(username)
        return render_template('username.html', user=USERS[index])
    abort(404)


    
@app.route('/users_new/',methods=['GET','POST'])
def newuser():
    app.logger.debug(request.args)
    return render_template('users_new.html',users=[USERS[i]["name"] for i in range(len(USERS))])


@app.route('/search/', methods=['GET'])
def search():
    app.logger.debug(request.args)
    app.logger.debug(request.args['pattern'])
    
    newlist=[]
    for name in [USERS[i]["name"] for i in range(len(USERS))]:
      if request.args['pattern'].lower() in name.lower():
        newlist.append(name)
    return render_template('users.html',users=newlist)


# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
