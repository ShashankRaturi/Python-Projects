class QuizBrain:
    def __init__(self , question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """
        returns whether any question is left or not
        """
        return self.question_number < len(self.question_list)    #returns boolean value
        


    def next_question(self):
        """
        this function returns the next question of the quiz.
        """
        current_question = self.question_list[self.question_number]
        number = self.question_number + 1

        user_answer = input("Q." + str(number)+ ": " + current_question.text + "(True/False : ?)")
        self.question_number += 1

        self.check_answer(user_answer , current_question.answer)
    
    def check_answer(self , user_answer , correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong.")

        print('The correct answer was: ' , correct_answer)
        print('Your current score is: {a}/{b}\n\n\n'.format(a = self.score , b = self.question_number))



   
    
