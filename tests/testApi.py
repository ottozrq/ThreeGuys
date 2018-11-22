import json
import urllib2
import dbServices as dbs
from pprint import *


def check_save(data, uid=""):
    req = urllib2.Request('http://vps613446.ovh.net/save/' + uid)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return response


def check_submit(data, uid=""):
    req = urllib2.Request('http://vps613446.ovh.net/submit/' + uid)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return response


if __name__ == '__main__':
    data = [{'content': "what's your name?", 'id_question': 1, 'ans_type': 'text'},
                 {'content': "what's your name?", 'id_question': 1, 'ans_type': 'text'}]
    # check_save(data)
    check_save(data)
    results = dbs.find_all()
    for result in results:
        pprint(result)
