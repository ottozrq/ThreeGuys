import dbServices as dbs
import dataModel as model
import uuid
from pprint import pprint
import json


def save(data, uid=""):
    save_flag = False
    if (uid == ""):
        uid = uuid.uuid1().hex
        save_flag = True
    respondent = model.Respondent(uid, False)
    for row in data:
        ans = model.Answer(row["id_question"], row["ans_type"], row["content"])
        respondent.add_answer(ans)
    if (save_flag):
        dbs.save(respondent)
    else:
        dbs.update(respondent, uid)
    return {"id": uid}


def submit(data, uid=""):
    save_flag = False
    if (uid == ""):
        uid = uuid.uuid1().hex
        save_flag = True
    respondent = model.Respondent(uid, True)
    for row in data:
        ans = model.Answer(row["id_question"], row["ans_type"], row["content"])
        respondent.add_answer(ans)
    if (save_flag):
        dbs.save(respondent)
    else:
        dbs.update(respondent, uid)
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


def getall():
    res_temp = {"submitted": True}
    respondents = dbs.find(res_temp)
    results = []
    for respondent in respondents:
        answers = respondent["answers"]
        his_answers = []
        for answer in answers:
            his_answer = model.Answer(answer["id_question"], answer["ans_type"], answer["content"])
            his_answers.append(his_answer)
        result = model.Respondent(respondent["id"], respondent["submitted"], his_answers)
        results.append(result)
    return results

if __name__ == "__main__":
    answer = model.Answer(1, "single choice", {"a_id": 1})
    answers = []
    answers.append(answer)
    answers.append(answer)
    submit(answers)
    results = dbs.find_all()
    for result in results:
        pprint(result)
    pprint(get(1))

