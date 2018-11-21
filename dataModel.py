import json


class Answer:
    def __init__(self, id_question, ans_type, content):
        self.id_question = id_question
        self.ans_type = ans_type
        self.content = content

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_json_obj(self):
        return json.loads(self.to_json_str())


class Respondent:
    def __init__(self, id, submitted, answers=[]):
        self.id = id
        self.submitted = submitted
        self.answers = answers

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
    answer = Answer(1, "text", "what's your name?")
    respondent = Respondent(1, False)
    respondent.add_answer(answer)
    respondent.add_answer(answer)
    print(respondent.to_string())
