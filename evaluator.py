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
            conversation += "Me: " + answer + "\n"

            if flag.strip() == "correct":
                i += 1
                print(feedback)
            else:
                question = feedback

        return feedback, flag

    def check_answer(self, topic, question, answer, conversation):
        prompt = f"""
            I am trying to learn {topic} by socratic method.

            Previous Conversation:
            {conversation}

            Latest Chat:
            AI: {question}
            Me: {answer}

            Based on the latest chat and context provided by previous conversation, check if the user answered the question correctly or not. If not, try to get the correct answer from the User.

            STRICTLY REPLY IN THE FOLLOWING FORMAT:
            <Your Response>
            @@@@
            correct|incorrect

            PLEASE FOLLOW THE FOLLOWING INSTRUCTIONS PROPERLY WITHOUT FAIL.
            NOTE: If I am correct return the correct flag
            NOTE: Return correct flag even if I am partially correct, but explain the missing points in your feedback
            NOTE: Ask a followup question to send me to the right direction if I am incorrect
            NOTE: Do not ask follow up for correct and partially correct answers
            NOTE: Provide feedback on my answer and tell in one word if it is correct or incorrect, separated by the delimiter @@@@
        """

        response = self.model.generate_content(prompt)

        try:
            feedback, flag = response.text.split("@@@@")
            flag = flag.strip()  # Clean up whitespace
        except ValueError:
            pass

        # Ensure flag is valid
        if flag.strip() not in ['correct', 'incorrect', 'partially correct']:
            print(flag)
            feedback = "Theer was an issue processing your answer. Please try again."
            flag = "incorrect"

        return feedback.strip(), flag.strip()



if __name__ == '__main__':
    evaluator = Evaluator()


