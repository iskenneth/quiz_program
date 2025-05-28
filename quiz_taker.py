#Quiz taker
#Import random
import random

#Flash the save questions, choices 
class Question:
    def __init__(self, text_question, choices, correct_answer):
        self.text_question = question
        self.choices = choices
        self.correct_answe = correct_answer
#check if the answer is right
    def right_answer(self, answer):
        return self.correct_answer == answer

def load_question_from_file(filename):
    question = []    
    with open ('quiz_data.txt', 'r') as file:
        lines = file.readlines()      
    for options in range (0,(len), 6):
                  