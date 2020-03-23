#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import request, make_response
from flask import render_template

app = Flask(__name__)


def deal_with_post():
    # Get the form content
    form = request.form
    app.logger.debug(dict(form))
    # Do whatever you need with the data
    # Returns code 201 for "created" status
    return 'Hello, World! You posted {}'.format(dict(form.items())), 201


@app.route('/hello_world', methods=['GET', 'POST'])
def hello_world():
    # You may use this logger to print any variable in
    # the terminal running the web server
    app.logger.debug('Running the hello_world function')
    app.logger.debug('Client request: method:"{0.method}'.format(request))
    if request.method == 'POST':
        # Use curl to post some data
        # curl -d"param=value" -X POST http://127.0.0.1:8000/hello_world
        return deal_with_post()
    # Open http://127.0.0.1:8000/hello_world?key=value&foo=bar&name=yourself
    # and have a look at the logs in the terminal running the server
    app.logger.debug('request arguments: {}'.format(request.args))
    if request.args:
        if 'name' in request.args.keys():
            # Use the query string argument to format the response
            return 'Hello {name} !'.format(**request.args), 200
    return 'Hello, World!', 200


@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('index.html')


@app.route('/about')
def about():
    app.logger.debug('about')
    today = datetime.today()
    # Create a context
    tpl_context = {}
    # Populate a context to feed the template
    # (cf. http://strftime.org/ for string formating with datetime)
    tpl_context.update({'day': '{:%A}'.format(today)})
    tpl_context.update({'d_o_month': '{:%d}'.format(today)})
    tpl_context.update({'month': '{:%B}'.format(today)})
    tpl_context.update({'time': '{:%X}'.format(today)})
    tpl_context.update({'date': today})
    # Now let's see how the context looks like
    app.logger.debug('About Context: {}'.format(tpl_context))
    return render_template('about.html', context=tpl_context)

@app.route('/Recherche')
def recherche():
  return render_template('recherche.html')

@app.route('/Stages')
def stages():
  return render_template('stages.html') 



@app.route('/test')
def test():
     resp = make_response('Thanks for all the fish', 501)
     resp.headers['X-My-Neat-Header'] = 'Foo/Bar'
     return resp
    #return 'Thanks for all the fish', 501


# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
