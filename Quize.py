class question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions_list = [

    "\n1. 10+5 = \n\na) 9\nb) 15\nc) 20\n",
    "\n2. 9-6 = \n\na) 5\nb) 7\nc) 3\n",
    "\n3. 20*7 = \n\na) 140\nb) 100\nc) 120\n",
    "\n4. 10/2 = \n\na) 1\nb) 5\nc) 2\n",

]

questions = [
    question(questions_list[0], "b"),
    question(questions_list[1], "c"),
    question(questions_list[2], "a"),
    question(questions_list[3], "b"),
]

def run_test(questions):
    score = 0
    for i in questions:
        if i.answer == input(i.question + "\nType Your Ans: "):
            score += 1
            print("Correct! " + str(score) + "/" + str(questions.index(i) + 1))
        else:
            print("Wrong! " + str(score) + "/" + str(questions.index(i) + 1))
    return score

print("\nYou Got: " + str(run_test(questions)) + "/" + str(len(questions)))
