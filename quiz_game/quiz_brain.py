class QuizBrain:
  
  #attributes function
  def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_list = q_list
  
 #check if there are more questions
  def still_question(self):
    #if the exceed the len, return true if match the following condiction
    return self.question_number < len(self.question_list)

  #check answer and
  #create next question based on question_bank passed by parameter
  def next_question(self):
    #set first question stored as current
    current = self.question_list[self.question_number]
    #set as question number 1
    self.question_number+=1
    #print Q.1: .... (True/False) and save input as user_answer
    user_answer = input(f"Q.{self.question_number}:{current.text} (True/False): ")
    #call function to see if they match and print score
    self.check_answer(user_answer, current.answer)
  
  #matching function
  def check_answer(self, user_answer, correct_answer):
    #if match
    if user_answer.lower()==correct_answer.lower():
      print("Right!")
      self.score +=1
    #not match
    else:
      print("Wrong")
      print(f"The correct answer was: {correct_answer}")
      print(f"Your current score is: {self.score}/{self.question_number}")