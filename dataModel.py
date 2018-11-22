import json
from pprint import pprint


class Answer:
    def __init__(self, id_question, ans_type, content):
        self.id_question = id_question
        self.ans_type = ans_type
        self.content = content

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_json_obj(self):
        return json.loads(self.to_json_str())

    def serialize(self):
        return {
            'id_question': self.id_question,
            'ans_type': self.ans_type,
            'content': self.content,
        }


class Respondent:
    def __init__(self, id, submitted, answers=[]):
        self.id = id
        self.submitted = submitted
        self.answers = answers


    def to_json_str_2(self):
        ans = json.dumps(self.answers, default=obj_dict)
        self.answers=[]
        resp = json.dumps(self)
        json_obj_ans = json.loads(ans)
        json_obj_resp = json.loads(resp)
        json_obj_resp['answers'].append(json_obj_ans)
        json_obj_resp
        return json.dumps(self.__dict__)

    def to_string(self):
        return json.dumps(self.to_json_obj())

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_json_obj(self):
        resp = Respondent(self.id, self.submitted, [])
        resp_str = resp.to_json_str()
        resp_json_obj = json.loads(resp_str)
        for ans in self.answers:
            answer_json_obj = ans.to_json_obj()
            resp_json_obj["answers"].append(answer_json_obj)
        return resp_json_obj

    def add_answer(self, answer):
        self.answers.append(answer)


if __name__ == "__main__":
    answer = Answer(1, "single choice", {"a_id": 1})
    respondent = Respondent(1, False)
    respondent.add_answer(answer)
    respondent.add_answer(answer)
    pprint(respondent.to_json_obj())
