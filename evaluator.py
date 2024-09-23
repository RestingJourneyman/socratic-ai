from dotenv import load_dotenv
from planner import Planner
import google.generativeai as genai
import os

load_dotenv()

class Evaluator:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API'))

        model_config = {
            "temperature": 0.2
        }

        self.model = genai.GenerativeModel("gemini-1.5-flash", generation_config=model_config)

    def __get_questions(self, topic):
        print("Genarating Plan...")
        pln = Planner()

        questions = pln.generate_questions(topic)

        return questions

    def start_study(self, topic):
        questions = self.__get_questions(topic)

        i = 0
        conversation = ""
        feedback = ""
        question = "Q"

        while i < len(questions):
            if question != feedback:
                question = questions[i]

            print(question)
            answer = input()
            feedback, flag = self.check_answer(topic, question, answer, conversation)

            conversation += "AI: " + question + "\n"
            conversation += "User: " + answer + "\n"

            if flag.strip() == "correct":
                i += 1
                print(feedback)
            else:
                question = feedback

    def check_answer(self, topic, question, answer, conversation):
        prompt = f"""
            User is trying to learn {topic} by socratic method.

            Previous Conversion:
            {conversation}

            Latest Chat:
            AI: {question}
            User: {answer}

            Based on latest chat and context provided by previous conversation check if the user answered the question correctly or not. If not try to get the correct answer from User.

            STRICTLY REPLY IN THE FOLLOWING FORMAT:
            <Your Response>
            @@@@
            correct|incorrect

            NOTE: Ask a followup to correct user if he is incorrect. if correct explain the concept a bit more
            NOTE: Only ask followup idf user is incorrect.
            NOTE: DO NOT ask a followup if user is correct. Only explaination is to be provided
            NOTE: Provide feedback on users answer and tell in one word if it is correct or not, seperated by the delimeter @@@@
        """

        response = self.model.generate_content(prompt)
        
        feedback, flag = response.text.split("@@@@")
        
        return feedback, flag

if __name__ == '__main__':
    evl = Evaluator()
    
    evl.start_study("bfs")