from flask import Flask, request, jsonify, render_template
from evaluator import Evaluator
from planner import Planner

app = Flask(__name__)

# Initialize the planner and evaluator
planner = Planner()
evaluator = Evaluator()

@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        Rendered HTML template for the main page.
    """
    return render_template('index.html')

# API to start study session (get questions)
@app.route('/start_study', methods=['POST'])
def start_study():
    """
    Start a study session by generating questions based on the selected topic.

    Request Parameters:
        - topic (str): The topic selected by the user.

    Returns:
        JSON response containing:
            - questions (list): A list of questions generated for the selected topic.
    """
    topic = request.form.get('topic')  # Get the topic from the form data
    questions = planner.generate_questions(topic)  # Generate questions using the planner
    return jsonify({"questions": questions})  # Return questions as a JSON response

# API to check the answer
@app.route('/check_answer', methods=['POST'])
def check_answer():
    """
    Check the user's answer against the correct answer and provide feedback.

    Request Body:
        - topic (str): The topic of the current question.
        - question (str): The current question being answered.
        - answer (str): The user's answer to the question.
        - conversation (list): A list of previous user responses for context.

    Returns:
        JSON response containing:
            - feedback (str): Feedback on the user's answer (e.g., "Correct", "Partial", "Incorrect").
            - flag (bool): A flag indicating whether the answer was correct or not.
    """
    data = request.get_json()  # Get the JSON data from the request
    topic = data['topic']  # Extract the topic
    question = data['question']  # Extract the question
    answer = data['answer']  # Extract the user's answer
    conversation = data['conversation']  # Extract the conversation history
    
    # Evaluate the answer using the evaluator
    feedback, flag = evaluator.check_answer(topic, question, answer, conversation)

    # Return the feedback and whether the answer was correct
    return jsonify({"feedback": feedback, "flag": flag})  # Return feedback as a JSON response

if __name__ == '__main__':
    app.run(debug=True)
