#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:31:43 2020

@author: tpoquillon
"""

from flask import request, abort, current_app, make_response
from flask import Blueprint, jsonify
from data import USERS
import json
SITE_API = Blueprint('api', __name__,)