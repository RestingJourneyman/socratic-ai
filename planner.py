from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

class Planner:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API'))

        model_config = {
            "temperature": 0.2
        }

        self.model = genai.GenerativeModel("gemini-1.5-flash", generation_config=model_config)

    def __plan_study(self, topic):
        response = self.model.generate_content(
            f"""
            Make a short module wise course on {topic}

            STRICTLY FOLLOW:
            End each module with the delimeter: @@@@
            Have no more than 3 modules
            """
        )
        
        modules = response.text.split("@@@@")

        if len(modules) <= 1:
            modules = response.text.split("****")
        
        if len(modules) <= 1:
            modules = response.text.split("Module")

        return modules

    def generate_questions(self, topic):
        modules = self.__plan_study(topic)
        course = []

        for module in modules:
            prompt = f"""
                For the following module, give me a list of questions to study the module from scratch by socratic method

                {module}

                STRICTLY FOLLOW THE FOLLOWING FORMAT:
                Q1:..
                @@@@
                Q2:...
                @@@@
                .
                .
                .
                Qn:...

                End each question each the delimeter: @@@@
                Formulate questions in layman terms and use only terms that has been uncovered
                Dont have any heading just a list of questions as in the given format
            """

            response = self.model.generate_content(prompt)
            
            questions = response.text.split("@@@@")
            course.extend(questions)

        return course

if __name__ == '__main__':
    pln = Planner()

    pln.generate_questions("sorting algorithms")