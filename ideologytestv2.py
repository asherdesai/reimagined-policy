# POLITICAL IDEOLOGY QUIZ v2

# economics: classifies user by preference of allocation: market or command economy, and by economic cohesiveness: individual or social preference of distribution
# foreign policy: classifies user by priorities: independence or passivism, strength or militarism or indispensability, and diplomacy or globalism
# state: classifies user by preference of state intervention/interaction in society: authoritarian or libertarianism
# society: classifies user by importance of cohesive national identity, immigration, etc., and by importance of traditional institutions and values, religion, etc.

# RUN PROGRAM TO START TEST

import math,os,csv

dir = "C:/Users/Asher/Desktop/python/.vscode"
os.chdir(dir)

class Question:
    def __init__(self, prompt, market, individual, independence, strength, diplomacy, authority, openness, tradition):
        self.prompt = prompt
        self.market = market
        self.individual = individual
        self.independence = independence
        self.strength = strength
        self.diplomacy = diplomacy
        self.authority = authority
        self.openness = openness
        self.tradition = tradition

    def __repr__(self):
        return f"{self.prompt}: {self.market}, {self.individual}, {self.independence}, {self.strength}, {self.diplomacy}, {self.authority}, {self.openness}, {self.tradition}\n"

class Ideology:
    def __init__(self, name, market, individual, independence, strength, diplomacy, authority, openness, tradition):
        self.name = name
        self.market = market
        self.individual = individual
        self.independence = independence
        self.strength = strength
        self.diplomacy = diplomacy
        self.authority = authority
        self.openness = openness
        self.tradition = tradition

    def __repr__(self):
        return f"{self.prompt}: {self.market}, {self.individual}, {self.independence}, {self.strength}, {self.diplomacy}, {self.authority}, {self.openness}, {self.tradition}\n"

questions_list = []
with open("questions_weights.txt", newline = "") as f:
    file_test_reader = csv.reader(f, delimiter = ",")
    for f in file_test_reader:
        questions_list.append(f)

questions = []
for item in questions_list:
    q = Question(item[0] + "\n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree", item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
    questions.append(q)

ideologies_list = []
with open("ideologies_metrics.txt", newline = "") as f:
    file_test_reader = csv.reader(f, delimiter = ",")
    for f in file_test_reader:
        ideologies_list.append(f)

ideologies = []
for item in ideologies_list:
    q = Ideology(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
    ideologies.append(q)

def match_ideology(metrics):
    print("The ideology with the smallest number is closest to yours.")
    for ideology in ideologies:
        ideology_metrics = [ideology.market, ideology.individual, ideology.independence, ideology.strength, ideology.diplomacy, ideology.authority, ideology.openness, ideology.tradition]
        ideology_metrics = [float(item) for item in ideology_metrics]
        similarity_v = [b - a for a, b in zip(metrics, ideology_metrics)]
        similarity_v = [i ** 2 for i in similarity_v]
        similarity = sum(similarity_v)
        try:
            similarity = math.sqrt(similarity)
        except ValueError:
            print("Value Error!")
        similarity = round(similarity)
        print("Your ideology has " + str(similarity) + " similarity to " + ideology.name + ".")

def run_test(questions):
    market = 0
    individual = 0
    authority = 0
    independence = 0
    strength = 0
    diplomacy = 0
    openness = 0
    tradition = 0
    metrics = [market, individual, independence, strength, diplomacy, authority, openness, tradition]
    agreement = 0
    for question in questions:
        question_metrics = [question.market, question.individual, question.independence, question.strength, question.diplomacy, question.authority, question.openness, question.tradition]
        question_metrics = [float(item) for item in question_metrics]
        agreement = ((int(input(question.prompt + "\n Answer: ")) - 3) / 2)
        question_metrics = [i * agreement for i in question_metrics]
        metrics = [a + b for a, b in zip(metrics, question_metrics)]
    metrics = [i * 100 for i in metrics]
    metrics = [round(i) for i in metrics]
    match_ideology(metrics)
    

def start_prompt():
    enter = input("POLITICAL IDEOLOGY QUIZ \nPress Enter to begin.")
    if enter == "":
        run_test(questions)
    else:
        print("You must press enter to begin the test.")
        start_prompt()

start_prompt()