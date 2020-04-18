#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:31:43 2020

@author: tpoquillon
"""

from flask import request, abort, current_app, make_response
from flask import Blueprint, jsonify
from data import DICO_STAGES
from data import MOTS_CLES
from data import GROUPES_MOTS_CLES
import json
SITE_API = Blueprint('api', __name__,)

@SITE_API.route('/api')
@SITE_API.route('/api/<string:node0>', methods=['GET'])
def api(node0=None):
  
    current_app.logger.debug(node0)
    if not node0:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)
    else:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)
      
@SITE_API.route('/api/telechargement', methods=['POST'])#télécharger les données d'un ou plusieurs stages au format json
def telechargement():
    req=request.args['liste']
    req_list=req.split(" ")
    index_list = list(map(int, req_list))
    Stages={DICO_STAGES[i]["sujet_stage"]:DICO_STAGES[i] for i in index_list}
    return jsonify(Stages)
    
    