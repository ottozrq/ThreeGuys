'''
class Question :
    def __init__(self, que_id, question, topic, subtopic, que_type, choices, sub_questions):
        self.que_id = que_id
        self.question = question
        self.topic = topic
        self.subtopic = subtopic
        self.que_type = que_type
        self.choices = choices
        self.sub_questions = sub_questions


class Choice :

    def __init__(self, ch_id, text, has_text_field):

        self.ch_id = ch_id
        self.text = text
        self.has_text_field = has_text_field
'''


class Answer:
    def __init__(self, id_question, ans_type, content):
        self.id_question = id_question
        self.ans_type = ans_type
        self.content = content


class Respondent:
    def __init__(self, res_id, submitted, answers=[]):
        self.res_id = res_id
        self.submitted = submitted
        self.answers = answers

