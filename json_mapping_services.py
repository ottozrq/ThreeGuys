import datamodel
import json
import pprint


def to_json(object):
    res = object.__dict__
    return res

def to_json_respondent(respondent):
    ans = json.dumps()
    res = json.dumps(respondent)
    res_obj = json.loads(res)
    ans_obj = json.loads(ans)
    res_ans = add_answers(res_obj, ans_obj)
    return res_ans


def add_answers(respondent_jsonobj, answer_jsonobj):
    respondent_jsonobj.answers.append(answer_jsonobj)
    return respondent_jsonobj


def to_object(json_data, res_object):
    res_object.__dict__ = json_data
    return res_object


if __name__ == "__main__":
    answer = datamodel.Answer(1, "text", "what's your name?")
    respondent = datamodel.Respondent(1, False)
    res = to_json_respondent(respondent)
    print(res)
