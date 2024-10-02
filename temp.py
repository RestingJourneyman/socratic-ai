from flask import Flask, request, jsonify, render_template
from evaluator import Evaluator
from planner import Planner

# app = Flask(__name__)

# Initialize the planner and evaluator
planner = Planner()
evaluator = Evaluator()
global topic
global i 
i = 0
global conversation
global feedback
conversation = ""
feedback = ""

# @app.route('/')
# def index():
#     return render_template('index.html')

# API to start study session (get questions)
# @app.route('/start_study', methods=['POST'])
def start_study(topic):
    # topic = request.form.get('topic')
    global questions
    questions = planner.generate_questions(topic)
    print(questions)
    # return jsonify({"questions": questions})

#API to check the answer
# @app.route('/check_answer', methods=['POST'])
def check_answer():
    data = {'topic:'}#request.get_json()
    topic = data['topic']
    question = data['question']
    answer = data['answer']
    conversation = data['conversation']
    feedback, flag = evaluator.check_answer(topic, question, answer, conversation)

    # Debugging output to check what the backend is returning
    print(f"Question: {question}, Answer: {answer}, Feedback: {feedback}, Flag: {flag}")

    #return jsonify({"feedback": feedback, "flag": flag})



if __name__ == '__main__':
    start_study("bfs")
    # check_answer()
    # app.run(debug=True
