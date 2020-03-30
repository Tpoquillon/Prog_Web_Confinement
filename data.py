# coding: utf-8

import json

from datetime import date, datetime

with open('data.json') as js:
    DATA = json.load(js)
    DICO_STAGES = DATA.get('DICO_STAGES')
    MOTS_CLES = DATA.get('MOTS_CLES')

def get_mots_cles(s_id):
    for mots_cles, ids in MOTS_CLES.items():
        if s_id in ids:
            yield mots_cles


for dico in DICO_STAGES:
    dico.update({'MOTS_CLES': [f for f in get_mots_cles(dico.get('id'))]})

# Script starts here
if __name__ == '__main__':
    pass

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
