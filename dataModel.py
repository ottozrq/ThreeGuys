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



class Text:
    def __init__(self, t_id, content):
        self.t_id = t_id
        self.content = content

    def serialize(self):
        return {
            't_id': self.t_id,
            'text': self.content,
        }

def dict(obj):
    return obj.__dict__

class Stat_answer:
    def __init__(self, a_id, number, texts=[]):
        self.a_id = a_id
        self.number = number
        self.texts = texts

    def to_json_str(self):
        texts = self.texts
        self.texts = []
        self_str = json.dumps(self.__dict__)
        text_str = json.dumps(texts,default=dict)
        self_obj = json.loads(self_str)
        text_obj = json.loads(text_str)
        self_obj['texts'].append(text_obj)
        self.texts = texts
        return json.dumps(self_obj)

    def to_json_obj(self):
        return json.loads(self.to_json_str())

    def serialize(self):
        res=[]
        for text in self.texts:
            res.append(text.serialize())
        return {
            'a_id': self.a_id,
            'number': self.number,
            'texts': res,
        }

class Respondent:
    def __init__(self, id, submitted, answers=[]):
        self.id = id
        self.submitted = submitted
        self.answers = answers


<<<<<<< HEAD
=======
    def to_json_str_2(self):
        ans = json.dumps(self.answers, default=obj_dict)
        self.answers=[]
        resp = json.dumps(self)
        json_obj_ans = json.loads(ans)
        json_obj_resp = json.loads(resp)
        json_obj_resp['answers'].append(json_obj_ans)
        json_obj_resp
        return json.dumps(self.__dict__)

>>>>>>> 83c56fd9f00e258127e6f0d2706136a388eef9ad
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



class Statistic:
    def __init__(self,q_id,type, q_content, answers=[]):
        self.q_id = q_id
        self.type = type
        self.q_content = q_content
        self.answers = answers

    def to_string(self):
            return json.dumps(self.to_json_obj())

    def to_json_str(self):
            return json.dumps(self.__dict__)

    def to_json_obj(self):
        stat = Statistic(self.q_id, self.type, self.q_content,[])
        stat_str = stat.to_json_str()
        stat_json_obj = json.loads(stat_str)
        for ans in self.answers:
            answer_json_obj = ans.to_json_obj()
            stat_json_obj["answers"].append(answer_json_obj)
        return stat_json_obj
'''
if __name__ == "__main__":
    answer = Answer(1, "single choice", {"a_id": 1})
    respondent = Respondent(1, False)
    respondent.add_answer(answer)
    respondent.add_answer(answer)
<<<<<<< HEAD
    print(respondent.to_string())
'''
if __name__ == "__main__":
    answer = Stat_answer(1, 1)
    test = Text(1, "sleepy")
    answer.texts.append(test)
    answer.texts.append(test)
    answer.texts.append(test)
    print answer.serialize()
=======
    pprint(respondent.to_json_obj())
>>>>>>> 83c56fd9f00e258127e6f0d2706136a388eef9ad
