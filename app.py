#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import abort, request, make_response
from flask import render_template
from data import DICO_STAGES
from data import MOTS_CLES
from data import GROUPES_MOTS_CLES

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
  return render_template('recherche.html',Groupeskeys=list(GROUPES_MOTS_CLES.keys()),Groupes=GROUPES_MOTS_CLES)


@app.route('/namesearch/', methods=['GET'])
def namesearch():
  New_List=[]
  for stage in [DICO_STAGES[i] for i in range(len(DICO_STAGES))]:
      if request.args['pattern'].lower() in stage["sujet_stage"].lower():
        New_List.append(stage)
  return render_template('stages.html',liste_stages=New_List)

@app.route('/keysearch/', methods=['GET'])
def keysearch():
  app.logger.debug(request)
  app.logger.debug(request.args.getlist("Mot_clef"))
  keylist=request.args.getlist("Mot_clef")
  Id_set=set([i for i in range(len(DICO_STAGES))])
  for key in keylist:
    Id_set=Id_set & set(MOTS_CLES[key])
  Id_List = list(Id_set)
  app.logger.debug(Id_List)
  Id_List.sort()
  New_list=[]
  for id in Id_List:
    New_list.append(DICO_STAGES[id])
  return render_template('stages.html',liste_stages=New_list)


@app.route('/Stages', methods=['GET','POST'])
@app.route('/stages/<stage_id>/', methods=['GET'])
def stages(stage_id=None):
  
  if not stage_id:
    return render_template('stages.html',liste_stages=DICO_STAGES) 
  elif int(stage_id) in [int(DICO_STAGES[i]["id"] )for i in range(len(DICO_STAGES))]:
    index = [int(DICO_STAGES[i]["id"])for i in range(len(DICO_STAGES))].index(int(stage_id))
    return render_template('stage.html', stage=DICO_STAGES[index])
  app.logger.debug(stage_id)
  app.logger.debug([DICO_STAGES[i]["id"] for i in range(len(DICO_STAGES))])
  abort(404)

#@app.route('/Stages', methods=['GET','POST'])
#def new_stage():
#    name = request.form['name']
#    sujet_stage = request.form['sujet_stage']
#    structure = request.form['structure']
#    ville = request.form['ville']
#    pays = request.form['pays']
#    structure = request.form['structure']
#    structure = request.form['structure']
    int i
    new_dico={"id": i,
     "sujet_stage": sujet_stage, "structure": structure, "ville": ville, 
     "pays": pays, "nom_eleve": nom_eleve , 
     "mail_eleve": mail_eleve, "nom_contact": nom_contact, 
     "mail_contact": mail_contact, "description": 
     description}
    DICO_STAGES.append(new_dico)
    

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
