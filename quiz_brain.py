import html,data
from question_model import Question

class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = self._get_questions()
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def _get_questions(self):
        
        questions = []
        question_data = data.get_questions()
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            questions.append(new_question)

        return questions


    def reset(self):
        self.question_number = 0
        self.score = 0
        self.question_list = self._get_questions()


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_question = f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"
        return user_question

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

