import dbServices as dbs
import dataModel as model
import uuid
from pprint import pprint
import json


def save(data):
    uid = uuid.uuid1().hex
    respondent = model.Respondent(uid, False, data)
    dbs.save(respondent)
    return {"id": uid}


def submit(data, uid=""):
    if (uid == ""):
        uid = uuid.uuid1().hex
    respondent = model.Respondent(uid, True, data)
    dbs.save(respondent)
    return {"id": uid}


def get(uid):
    respondent = dbs.find_one(uid)
    if (not respondent):
        return {"error": "No such sheet."}
    if (respondent["submitted"]):
        return {"error": "The sheet has already been submitted."}
    answers = respondent["answers"]
    results = []
    for answer in answers:
        result = model.Answer(answer["id_question"], answer["ans_type"], answer["content"])
        results.append(result)
    return results


if __name__ == "__main__":
    answer = model.Answer(1, "text", "what's your name?")
    answers = []
    answers.append(answer)
    answers.append(answer)
    submit(answers)
    results = dbs.find_all()
    for result in results:
        pprint(result)
    pprint(get(1))

