from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:

    question = i["text"]
    answer = i["answer"]

    new_question = Question(question , answer)   #creating object of that question
    question_bank.append(new_question) #appending it to question bank thereby making list of objects


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz.')
print('Your final score was: {a}/{b}'.format(a = quiz.score , b = quiz.question_number))