from pymongo import *
import logging
import json_mapping_services
from datamodel import *
from pprint import *

client = MongoClient(host='localhost', port=27017)
db = client.Three_guys
collection = db.answers
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def save(respondent):
    respondent_json = json_mapping_services.to_json(respondent)
    result = collection.insert_one(respondent_json)
    logger.info(result)


def find(respondent):
    to_find = {'res_id': respondent.res_id}
    result = collection.find_one(to_find)
    logger.info(result)
    return result


def update(respondent,to_update):
    respondent_json = json_mapping_services.to_json(respondent)
    to_find = {'res_id': to_update.res_id}
    result = collection.update_one(to_find, {'$set': respondent_json})
    logger.info(result)

def delete(respondent):
    to_delete = {'respondent_id': respondent.res_id}
    result = collection.delete_one(to_delete)
    logger.info(result)


if __name__ == "__main__":
    answer = Answer(1, "text", "what's your name?")
    answers = [answer]
    respondent = Respondent(1, False, answers)
    answer2 = Answer(1, "text", 'my name is qiaoyu.liu')
    json_mapping_services.add_answers(respondent, answer2)
    answers = []
    to_update = Respondent(1, False, answers)
    save(respondent)
    pprint(find(respondent))
    update(respondent, to_update)
    pprint(find(to_update))
    delete(to_update)
    pprint(find(to_update))
