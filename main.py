from dotenv import load_dotenv
from planner import Planner
import os

load_dotenv()

pln = Planner()
questions = pln.generate_questions("sorting algorithms")

for ques in questions:
    print(ques)