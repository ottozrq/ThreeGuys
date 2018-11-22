from pymongo import *
import logging
from dataModel import *
from pprint import *

client = MongoClient(host='localhost', port=27017)
db = client.Three_guys
collection = db.answers
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def save(respondent):
    respondent_json = respondent.to_json_obj()
    result = collection.insert(respondent_json)
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


def update(respondent, uid):
    respondent_json = respondent.to_json_obj()
    to_find = {'id': uid}
    result = collection.update_one(to_find, {'$set': respondent_json})
    logger.info(result)


def delete(respondent):
    to_delete = {'id': respondent.id}
    result = collection.delete_one(to_delete)
    logger.info(result)


if __name__ == "__main__":
    answer = Answer(1, "text", "what's your name?")
    answers = [answer]
    respondent = Respondent(1, False, answers)
    answer2 = Answer(1, "text", 'my name is qiaoyu.liu')
    respondent.add_answer(answer2)
    answers = []
    to_update = Respondent(1, False, answers)
    save(respondent)
    pprint(find_one(respondent))
    update(respondent, to_update)
    pprint(find_one(to_update))
    delete(to_update)
    pprint(find_all())