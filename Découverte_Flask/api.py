# coding: utf-8

from flask import request, abort, current_app, make_response
from flask import Blueprint, jsonify
from data import USERS
import json
SITE_API = Blueprint('api', __name__,)

@SITE_API.route('/api')
@SITE_API.route('/api/<string:node0>', methods=['GET'])
def api(node0=None):
    if not node0:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)
    elif node0 in ["users","users"]:
      return jsonify([USERS[i]["name"] for i in range(len(USERS))])
    else:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)

@SITE_API.route('/api/users/<name>', methods=['GET'])
def api_user(name=None):
  req=request.headers
  current_app.logger.debug("you are in api_user")
  if name in [USERS[i]["name"] for i in range(len(USERS))]:
    current_app.logger.debug('Looking at "{}" resource'.format(name))
    index = [USERS[i]["name"] for i in range(len(USERS))].index(name)
    if "Accept" in req and "text/plain" in req["Accept"]:
      response = make_response(str(USERS[index]))
      response.headers['Content-Type'] = "text/plain"
      return response
    else: 
      response = make_response(jsonify(USERS[index]))
      response.headers['Content-Type'] = "application/json"

      return response
  else:
    current_app.logger.debug('Looking at "{}" resource'.format(name))
    abort(404)

@SITE_API.route('/api/users/', methods=['GET'])
def api_users_request():
    current_app.logger.debug(request.args)
    Reqfields=[k for k in request.args.keys()]
    current_app.logger.debug([k for k in request.args.keys()])
    #current_app.logger.debug(request.args['pattern'])
    fields =["gender"]
    Req=[]
    for req in Reqfields:
      if req in fields:
        Req.append(req)
    newlist=[]
    for i in range(len([USERS[i]["name"] for i in range(len(USERS))])):
      B=True
      for req in Req:
        if request.args[req]!=USERS[i][req]:
          B=False
      if B:
        newlist.append([USERS[i]["name"] for i in range(len(USERS))][i])
    return jsonify(newlist)
  
  
@SITE_API.route('/api/users/<name>', methods=['PUT'])
def api_modify_user(name=None):
  index = [USERS[i]["name"] for i in range(len(USERS))].index(name)
  if index != -1:
    current_app.logger.debug(request.data)
    dic= json.loads(request.data)
    keys= [k for k in dic]
    for key in keys:
      USERS[index][key]=dic[key]
      if "name in keys":
        [USERS[i]["name"] for i in range(len(USERS))][index]=dic["name"]
        response = make_response("Done")
    return response 
  abort(404)
  
@SITE_API.route('/api/users', methods=['POST'])
def api_add_user():
  dic= json.loads(request.data)
  USERS.append(dic)
  return("done",200)
# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
