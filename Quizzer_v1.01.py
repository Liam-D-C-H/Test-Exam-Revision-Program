from copy import deepcopy
import random
import string
"""
    @author Liam Hope
    @additional_credits Some changes made by Reno
    @since 2/11/2015.
    @modified 2/11/2015
    @description This is the quizzer for exam and test revision. It's basic for now but will likely be later updated
    @description with more features. Make sure to follow the format of the text files, and do not have a blank
    @description line at the end.
"""


class Quizzer:

    def __init__(self):
        self._linesOfQuestionsFile = []
        self._numberOfQuestionsAvaliable = 0
        self._showAnswerIfWrong = False #aka -S
        self._continuePastLastQuestion = False #aka -C

        random.seed()
        self._load_answer_file()
        self._setup_options()
        self.menu()



    def menu(self):
        while True: #continues until it is exited
            selection = 0
            while True:
                try:
                    print("Please select from the following options:")
                    print("1. Answer questions")
                    print("2. Load in additional question files")
                    print("3. Empty the questions list and start from a new one")
                    print("4. Set up options")
                    print("5. Exit the menu")
                    selection = int(input())
                    if selection <1 or selection >5:
                        raise ValueError
                    break
                except:
                    print("Please enter an integer from 1 to 5 \n")
            if selection==1:    #Answer questions
                self._answer_questions()
            if selection==2:    #Load in additional question files
                self._load_answer_file()
            if selection==3:    #Empty the questions list and start from a new one
                self._linesOfQuestionsFile = []
                self._load_answer_file()
            if selection==4:    #Set up options
                self._setup_options()
            if selection==5:    #Exit the menu
                break

    def _load_answer_file(self):
        while True:
            try:
                in_file_name = input("Please enter the name of the next file you want to add containing questions \n")
                in_file = open(in_file_name, "r")
                self._linesOfQuestionsFile += in_file.readlines()
                if input("Are you done?, enter Y for yes \n").upper() == "Y":
                    break
            except FileNotFoundError:
                print("Please enter a valid file name")
        self._numberOfQuestionsAvaliable = len(self._linesOfQuestionsFile)//6

    def _answer_questions(self):
        number_of_questions = 0
        while True:
            if self._continuePastLastQuestion == True:
                number_of_questions = int(input("Please enter the number of questions you want to answer, up to 500 \n"))
                if number_of_questions <= 500 and number_of_questions > 0:
                    break
                else:
                    print("Please enter a valid number of questions")
            else:
                number_of_questions = int(input("Please enter the number of questions you want to answer, up to " + str(self._numberOfQuestionsAvaliable) + " \n"))
                if number_of_questions <= self._numberOfQuestionsAvaliable and number_of_questions > 0:
                    break
                else:
                    print("Please enter a valid number of questions")
        #questions_remaining = deepcopy(number_of_questions)
        no_of_right_answ = 0
        no_of_wrong_answ = 0
        questions = []
        for i in range(number_of_questions):
            retVal, no_of_right_answ, no_of_wrong_answ  = self._multiple_choice_questions(questions, no_of_right_answ, no_of_wrong_answ)
            if retVal == "stop questions":
                break
        print("You got " + str(no_of_right_answ) + " right")
        print("You got " + str(no_of_wrong_answ) + " wrong")
        print("This means that you answered " + str(100/(no_of_right_answ+no_of_wrong_answ)*no_of_right_answ) + "% of the questions correctly")

    def _get_correct_answer(self, current_question_start_line):
        char_number = 0
        while True:
            if self._linesOfQuestionsFile[current_question_start_line+5][char_number] == " ":
                return self._linesOfQuestionsFile[current_question_start_line+5][char_number+1]
            else:
                char_number += 1

    def _setup_options(self):
        print("Enter the options you would like enabled in a single line, just press enter for no options")
        print("Type -S to show the correct answer after you answer a question incorrectly")
        print("Type -C to allow for more rounds of questions than there are questions")
        commands = input()
        if "-S" in commands or "-s" in commands:
            self._showAnswerIfWrong = True
        else:
            self._showAnswerIfWrong = False
        if "-C" in commands or "-c" in commands:
            self._continuePastLastQuestion = True
        else:
            self._continuePastLastQuestion = False

    def _multiple_choice_questions(self, questions, no_of_right_answ, no_of_wrong_answ):
        current_question_number = random.randint(1,self._numberOfQuestionsAvaliable)
        if len(questions) == self._numberOfQuestionsAvaliable:
            if self._continuePastLastQuestion:
                questions.clear()
            else:
                return ("stop questions", no_of_right_answ, no_of_wrong_answ)
        while current_question_number in questions:
            current_question_number = random.randint(1,self._numberOfQuestionsAvaliable)
        #if current_question_number not in questions:
        current_question_start_line = (current_question_number-1)*6
        questions.append(current_question_number)
        print(self._linesOfQuestionsFile[current_question_start_line])
        for j in range(1,5):
            print(self._linesOfQuestionsFile[current_question_start_line+j])
        answer = input("Please enter A, B, C or D \n").upper()
        correct_answer = self._get_correct_answer(current_question_start_line)
        if answer == correct_answer:
            print("Correct\n")
            no_of_right_answ += 1
        else:
            print("Incorrect")
            no_of_wrong_answ += 1
            if self._showAnswerIfWrong:
                print("Correct answer is " + correct_answer + "\n")
        return (0, no_of_right_answ, no_of_wrong_answ)



if __name__ == "__main__":
    q1 = Quizzer()


