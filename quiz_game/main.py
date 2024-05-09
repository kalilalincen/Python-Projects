from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#initia empyty list
question_bank = []

#loop through dic to get text and answer
for i in question_data:
    #extract the information from dataset
    question_text = i["text"]
    question_answer = i["answer"]
    #create a new question using the info extracted
    new_q = Question(question_text, question_answer)
    #add to question_bank
    question_bank.append(new_q)

#feed the question_bank list into QuizBrain class and store es quiz
quiz = QuizBrain(question_bank)

#iteratively print question and match answer, and next question and next question, until no remaining question
while quiz.still_question():
    quiz.next_question()

#print the result
print(f"You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")