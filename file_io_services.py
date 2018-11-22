import dataModel as model
import dbServices as dbs
import json

def statistic_db_maker():
    with open("data/questions.json","r") as json_f:
        load_dict = json.load(json_f)
        i = 1
        for ele in load_dict:
            question = question_maker(ele,i)
            i += 1
            if ele['subquestions']!= []:
                for sub_ele in ele['subquestions']:
                    question = question_maker(sub_ele,i)
                    i += 1
            dbs.save_stat(question)
            i+=1

def question_maker(ele,i):
    question = model.Statistic(i, ele['type'], ele['question'])
    j = 1
    for choice in ele['choices']:
        stat_answer = model.Stat_answer(j, 0)
        question.answers.append(stat_answer)
        j += 1
    return question

if __name__ == "__main__":
    statistic_db_maker()