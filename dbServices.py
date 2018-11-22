from pymongo import *
import logging
from dataModel import *
from pprint import *

client = MongoClient(host='localhost', port=27017)
db = client.Three_guys
collection = db.answers
stcollection = db.statistic
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def save(respondent):
    respondent_json = respondent.to_json_obj()
    result = collection.insert(respondent_json)
    logger.info(result)


def save_stat(statistic):
    stat_json = statistic.to_json_obj()
    result = stcollection.insert(stat_json)
    logger.info(result)


def find_one(uid):
    to_find = {'id': uid}
    result = collection.find_one(to_find)
    logger.info(result)
    return result


def find_all():
    result = collection.find()
    logger.info(result)
    return result


def find(respondent):
    result = collection.find(respondent)
    logger.info(result)
    return result

def find_stat(answer):
    to_find = {'q_id': answer.id_question}
    result = stcollection.find_one(to_find)
    logger.info(result)
    return result

def update(respondent, uid):
    respondent_json = respondent.to_json_obj()
    to_find = {'id': uid}
    result = collection.update_one(to_find, {'$set': respondent_json})
    logger.info(result)

def updata_stat(statistic):
    stat_json = statistic.to_json_obj()
    to_find = {'q_id': statistic.q_id}
    result = stcollection.update_one(to_find, {'$set': stat_json})
    logger.info(result)

def delete(respondent):
    to_delete = {'id': respondent.id}
    result = collection.delete_one(to_delete)
    logger.info(result)


if __name__ == "__main__":
    answer = Answer(1, "SC", {"a_id": 1})
    answers = [answer]
    respondent = Respondent(1, False, answers)
    answer2 = Answer(2, "T", 'my name is qiaoyu.liu')
    respondent.add_answer(answer2)
    answer3 = Answer(3, "MC", {"a_id": [1, 2, 3]})
    respondent.add_answer(answer3)
    answer4 = Answer(4, "ST", {"a_id": 1, "text": "hahaha"})
    respondent.add_answer(answer4)
    answers = []
    to_update = Respondent(2, False, answers)
    save(respondent)
    pprint(find_one(2))
    results = find_all()
    for result in results:
        pprint(result)
    # update(respondent, to_update)
    # pprint(find_one(2))
    # delete(to_update)
    # pprint(find_all())