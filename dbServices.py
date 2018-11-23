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


def delete(uid):
    to_delete = {'id': uid}
    result = collection.delete_many(to_delete)
    logger.info(result)


if __name__ == "__main__":
    answer = Stat_answer(1, 1)
    test = Text(1, "sleepy")
    answer.texts.append(test)
    answer.texts.append(test)
    answer.texts.append(test)
    answers = [answer]
    stat = Statistic(1,1,"aaaaaaaaaaaaa",answers)
    save_stat(stat)
