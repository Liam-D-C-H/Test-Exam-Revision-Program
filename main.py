from copy import deepcopy
import random
import string
"""
    @author Liam Hope
    @additional_credits None atm
    @since 2/11/2015.
    @modified 2/11/2015
    @description This is the quizzer for exam and test revision. It's basic for now but will likely be later updated
    @description with more features. Make sure to follow the format of the text files, and do not have a blank
    @description line at the end.
"""


class Quizzer:

    def __init__(self):
        self.linesOfQuestionFile = []
        self.numberOfQuestionsAvaliable = 0
        self.load_answer_file()
        self.mathMode = False
        random.seed()

    def load_answer_file(self):
        while True:
            try:
                in_file_name = input("Please enter the name of the next file you want to add containing questions \n")
                in_file = open(in_file_name, "r")
                self.linesOfQuestionFile += in_file.readlines()
                command = input("Are you done?, enter Y for yes, enter M for done & FIT1031 CH2 Math mode \n")
                if command== "M":
                    self.mathMode = True
                    break
                if command== "Y":
                    break
            except:
                print("Please enter a valid file name")
        self.numberOfQuestionsAvaliable = len(self.linesOfQuestionFile)//6

    def answer_questions(self):
        while True:
            try:
                number_of_questions = int(input("Please enter the number of questions you want to answer, up to 500 \n"))
                if number_of_questions <= 500 and number_of_questions > 0:
                    break
                else:
                    print("Please enter a valid number of questions")
            except:
                print("Please enter a valid number of questions")
        questions_remaining = deepcopy(number_of_questions)
        no_of_right_answ = 0
        no_of_wrong_answ = 0
        for i in range (questions_remaining):
            if self.mathMode:
                self._ask_maths_questions()
            else:
                self._ask_multiple_choice(no_of_right_answ, no_of_wrong_answ)

        print("You got " + str(no_of_right_answ) + " right")
        print("You got " + str(no_of_wrong_answ) + " wrong")
        print("This means that you answered " + str(100/(no_of_right_answ+no_of_wrong_answ)*no_of_right_answ) + "% of the questions correctly")

    def _get_correct_answer(self, current_question_start_line):
        char_number = 0
        while True:
            if self.linesOfQuestionFile[current_question_start_line+5][char_number] == " ":
                return self.linesOfQuestionFile[current_question_start_line+5][char_number+1]
            else:
                char_number += 1

    def _ask_multiple_choice(self, no_of_right_answ, no_of_wrong_answ):
            current_question_number = random.randint(1,self.numberOfQuestionsAvaliable)
            current_question_start_line = (current_question_number-1)*6
            print(self.linesOfQuestionFile[current_question_start_line])
            for j in range (1,5):
                print(self.linesOfQuestionFile[current_question_start_line+j])
            answer = input("Please enter A, B, C or D \n")
            correct_answer = self._get_correct_answer(current_question_start_line)
            if answer == correct_answer:
                print("Correct")
                no_of_right_answ += 1
            else:
                print("Incorrect")
                no_of_wrong_answ += 1

    def _ask_maths_questions(self):
        question_type = random.randint(1,1)
        if question_type == 1:
            pass    #WIP

        #unsigned int question
        #signed magnitude int question
        #two's compliment question
        #excess-k question
        #floating point question
        #decimal to binary question
        #binary to decimal question
        #hex to binary question
        #binary to hex question
        #decimal to hex question
        #hex to decimal question



if __name__ == "__main__":
    q1 = Quizzer()
    q1.answer_questions()


