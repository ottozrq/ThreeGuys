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

def update_stat(answer):
    type = answer.ans_type
    ans_content = answer.content
    res_ans = dbs.find_stat(answer)
    stat = model.Statistic(answer.id_question, type, res_ans['q_content'])
    choices = res_ans['answers']
    if type ==4:
        choices.append(ans_content)
    else:
     for choice in choices:
        texts = choice['texts']
        if ans_content['a_id'] == choice['a_id']:
            if type == 3:
               i = 0
               for ele in texts:
                 i += 1
               text = model.Text(i,ans_content['text'])
               texts.append(text)
               stat_answer = model.Stat_answer(choice['a_id'],choice['number']+1,texts)
            if type == 1:
               stat_answer = model.Stat_answer(choice['a_id'], choice['number'] + 1)
        if type==2 and  choice['a_id'] in ans_content['a_id'] :
            stat_answer = model.Stat_answer(choice['a_id'], choice['number'] + 1)
        else :
            stat_answer = model.Stat_answer(choice['a_id'],choice['number'],texts)
        stat.answers.append(stat_answer)
    dbs.updata_stat(stat)
    return


def submit(data, uid=""):
    save_flag = False
    if (uid == ""):
        uid = uuid.uuid1().hex
        save_flag = True
    respondent = model.Respondent(uid, True)
    for row in data:
        ans = model.Answer(row["id_question"], row["ans_type"], row["content"])
        update_stat(ans)
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
    respondents = dbs.find_all()
    results = []
    for respondent in  respondents:
        answers = respondent["answers"]
        his_answers = []
        for answer in answers:
            his_answer = model.Answer(answer["id_question"], answer["ans_type"], answer["content"])
            his_answers.append(his_answer)
        result = model.Respondent(respondent["id"], respondent["submitted"], his_answers)
        results.append(result)
    return results

'''
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

'''
if __name__ == "__main__":
    answer = model.Answer(1, 1, {'a_id':1,})
    update_stat(answer)