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
    if not node0:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)
    elif node0 in ["stages","Stages"]:
      return jsonify([DICO_STAGES[i]["sujet_stage"] for i in range(len(DICO_STAGES))])
    else:
      current_app.logger.debug('Looking at "{}" resource'.format(node0))
      abort(501)