import json
import urllib2
import dbServices as dbs
from pprint import *

url = "http://localhost:5000"


def check_save(data, uid=""):
    req = urllib2.Request(url + '/save/' + uid)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return response.read()


def check_submit(data, uid=""):
    req = urllib2.Request(url + '/submit/' + uid)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return response


if __name__ == '__main__':
    data = [{'ans_type': 'SC',
             'content': {'a_id': 1},
             'id_question': 1},
            {'ans_type': 'T',
             'content': 'my name is qiaoyu.liu',
             'id_question': 2},
            {'ans_type': 'MC',
             'content': {'a_id': [1, 2, 3]},
             'id_question': 3},
            {'ans_type': 'ST',
             'content': {'a_id': 1, 'text': 'hahaha'},
             'id_question': 4}]

    # check_save(data)
    print check_save(data)
    results = dbs.find_all()
    for result in results:
        pprint(result)
