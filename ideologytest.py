# POLITICAL IDEOLOGY QUIZ

# economics: classifies user by preference of allocation: market or command economy, and by economic cohesiveness: individual or social preference of distribution
# foreign policy: classifies user by priorities: independence or passivism, strength or militarism or indispensability, and diplomacy or globalism
# state: classifies user by preference of state intervention/interaction in society: authoritarian or libertarianism
# society: classifies user by importance of cohesive national identity, immigration, etc., and by importance of traditional institutions and values, religion, etc.

# RUN PROGRAM TO START TEST

import math

class question:
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
        # defines class question with parameters prompt and one for each metric

class ideology:
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

question_prompts = [
    "A market economy is better than a planned economy. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "The government should not use taxes to redistribute wealth to the needy. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "We should focus on issues at home before participating in global affairs. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "We should use our military strength to protect our interests abroad. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "It is often important to compromise with allies to ensure global peace and stability. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "I feel more safe when the government has more power to protect me. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "Everyone having the same ethnicity is an integral part of national identity. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree",
    "We should preserve traditional institutions like religion. \n5 - strongly agree \n4 - agree \n3 - neutral \n2 - disagree \n1 - strongly disagree"
]

ideology_names = [
    "neoliberalism",
    "neoconservatism",
    "democratic socialism",
    "national socialism",
    "maoism/stalinism"
]

questions = [
    question(question_prompts[0], 0.9, 0, 0, 0, 0, -0.1, 0, 0),
    question(question_prompts[1], 0.1, 1, 0, 0, 0, -0.1, 0, 0),
    question(question_prompts[2], 0, 0, 0.7, -0.3, -0.3, 0, 0, 0),
    question(question_prompts[3], 0, 0, -0.3, 0.7, -0.3, 0, 0, 0),
    question(question_prompts[4], 0, 0, -0.3, -0.3, 0.7, 0, 0, 0),
    question(question_prompts[5], 0, 0, 0, 0, 0, 0.8, 0, 0),
    question(question_prompts[6], 0, 0, 0, 0, 0, 0, -1, 0),
    question(question_prompts[7], 0, 0, 0, 0, 0, 0, 0, 1)
]

ideologies = [
    ideology(ideology_names[0], 90, 0, -100, 0, 100, -10, 100, -50),
    ideology(ideology_names[1], 100, 100, -100, 100, 0, 20, 0, 50),
    ideology(ideology_names[2], -10, -100, 50, -100, 50, 50, 100, 50),
    ideology(ideology_names[3], -5, -50, 50, 50, -100, 85, -100, 100),
    ideology(ideology_names[4], -100, -100, 65, -35, -35, 100, 0, -100)
]

def match_ideology(metrics):
    print("The ideology with the smallest number is closest to yours.")
    for ideology in ideologies:
        ideology_metrics = [ideology.market, ideology.individual, ideology.independence, ideology.strength, ideology.diplomacy, ideology.authority, ideology.openness, ideology.tradition]
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