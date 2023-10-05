# import random

# # Define a list of questions and their corresponding answers
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["a) Paris", "b) London", "c) Rome"],
#         "answer": "a"
#     },
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["a) Earth", "b) Mars", "c) Venus"],
#         "answer": "b"
#     },
#     {
#         "question": "What is the largest mammal in the world?",
#         "options": ["a) Elephant", "b) Giraffe", "c) Blue Whale"],
#         "answer": "c"
#     }
# ]

# # Function to shuffle the questions randomly
# def shuffle_questions(questions):
#     random.shuffle(questions)

# # Function to display a question and its options
# def display_question(question_data):
#     print(question_data["question"])
#     for option in question_data["options"]:
#         print(option)

# # Function to get the user's answer
# def get_user_answer():
#     return input("Enter your answer (a/b/c): ").strip().lower()

# # Function to check if the user's answer is correct
# def is_correct(user_answer, correct_answer):
#     return user_answer == correct_answer

# # Function to run the quiz
# def run_quiz(questions):
#     shuffle_questions(questions)
#     score = 0

#     for question_data in questions:
#         display_question(question_data)
#         user_answer = get_user_answer()
#         if is_correct(user_answer, question_data["answer"]):
#             print("Correct!\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {question_data['answer'].upper()}\n")

#     print(f"You got {score} out of {len(questions)} questions correct!")

# # Main function
# if __name__ == "__main__":
#     print("Welcome to the General Knowledge Quiz!")
#     # run_quiz(questions)
#     print(random.shuffle(questions))


import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def display_question(self, question):
        print(question.question)
        for option in question.options:
            print(option)

    def get_user_answer(self):
        return input("Enter your answer (a/b/c): ").strip().lower()

    def is_correct(self, user_answer, correct_answer):
        return user_answer == correct_answer

    def run(self):
        self.shuffle_questions()

        print("Welcome to the Object-Oriented Programming Quiz!")

        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()

            if self.is_correct(user_answer, question.answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question.answer.upper()}\n")

        print(f"You got {self.score} out of {len(self.questions)} questions correct!")

if __name__ == "__main__":
    oop_questions = [
        Question("What is an object in OOP?", ["a) A variable", "b) An instance of a class", "c) A function"], "b"),
        Question("What is inheritance in OOP?", ["a) Passing attributes to a function", "b) Reusing a class's attributes and methods in another class", "c) Creating new attributes"], "b"),
        Question("What does 'self' refer to in Python classes?", ["a) The current module", "b) The instance of the class", "c) A reserved keyword"], "b"),
        Question("What is encapsulation in OOP?", ["a) Hiding the implementation details of an object", "b) Creating new objects", "c) Inheriting from a base class"], "a"),
        Question("What is a constructor in Python?", ["a) A method to create new objects", "b) A type of variable", "c) A reserved keyword"], "a"),
        Question("What is polymorphism in OOP?", ["a) Having multiple constructors", "b) The ability of objects to take on many forms", "c) The process of data hiding"], "b"),
        Question("What is a class variable in Python?", ["a) A variable defined inside a method", "b) A variable shared by all instances of a class", "c) A global variable"], "b"),
        Question("What is a method in OOP?", ["a) A function that is not part of a class", "b) A function defined inside a class", "c) A variable"], "b"),
        Question("What is a subclass in OOP?", ["a) A class with no attributes", "b) A class that inherits from another class", "c) A class that cannot have methods"], "b"),
        Question("What is an abstract class in Python?", ["a) A class that cannot be inherited", "b) A class that can have both concrete and abstract methods", "c) A class with no methods"], "b"),
    ]

    quiz = Quiz(oop_questions)
    quiz.run()