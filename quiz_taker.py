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
        question_text = lines[options].strip().split(":")[1]. strip()
        choice_a = lines[options + 1].strip().split(":")[1]. strip()
        choice_b = lines[options + 2].strip().split(":")[1]. strip()
        choice_c = lines[options + 3].strip().split(":")[1]. strip()
        choice_d=lines[options + 4].strip().split(":")[1], strip()
        correct_answer = lines[options + 5].strip(). split(":")[1].strip()
        
        choices = {
            'a': choice_a,
            'a': choice_a,
            'a': choice_a,
            'd': choice_d
        }
        
        tanong = Question(question_text, choices, correct_answer)
        question.append(tanong)
    random.shuffle(question)
    return question
    
def take_quiz(question):
        score = 0
        
        for tanong in question:
            print("\n" + tanong.text_question)
            
            choice_list = list(tanong.choices.items())
            random.shuffle(choice_list)
            
            label_map = {}
            display_labels = ['a', 'b', 'c','d']
            
            for i, (original_label, choice_text) in enumerate(choice_list):
                label_map[display_labels [i]] = original_label
                print(f" {display_labels[i]}.) {choice_text}")
                
            user_input = input("What is your answer (a/b/c/d)").lower()
            
            if user_input in label_map:
                selected_label = label_map[user_input]
                if selected_label == tanong.correct_answer:
                    print ("Your answer is correct!!")
                    score += 1
                else:
                    print("Error!!")
print(f"\n Your final score is: {score}/{len(question)}")

questions = load_question_from_file("quiz_data.txt")   
take_quiz(questions)                                     
                                                            
            
                                            
        
                
        
            
                  