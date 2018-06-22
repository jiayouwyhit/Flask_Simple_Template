'''
    The RESTful style api server
'''
from flask import render_template
from flask import Flask, request, redirect, jsonify, send_from_directory
from server import app

import random


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getRecQuestions', methods=['GET', 'POST'])
def get_recommended_question_list():
    print('/getRecQuestions')

    input_status = 'Great! You have input the correct variables!'
    if request.json != None:
        print('request.json: ', request.json)
        user_id = request.json.get('user_id')
        current_problem = request.json.get('current_problem')
        previous_sequence = request.json.get('previous_sequence')
    elif request.form != None:
        print('request.form: ', request.form)
        user_id = request.form.get('user_id')
        current_problem = request.form.get('current_problem')
        previous_sequence = request.form.get('previous_sequence')
    else:
        input_status = 'Error! You have not correctly submit the input variables!'
    
    if user_id == None or current_problem == None or previous_sequence == None:
        input_status = 'Error! You have not correctly submit the input variables!'

    # TO-DO: Add the processing functions here

    # Send back the result
    similar_problems = generate_random_question_ids()
    pre_ordered_problems = generate_random_question_ids()
    advanced_problems = generate_random_question_ids()


    rec_question_list = {
        'input_status': input_status, 
        'similar_problems': similar_problems, 
        'pre_ordered_problems': pre_ordered_problems, 
        'advanced_problems': advanced_problems}
    return jsonify(rec_question_list)


def generate_random_question_ids():
    base_question_id = 126171
    max_range = 209
    recom_num = 5

    tmp = []
    for i in range(5):
        q_id = base_question_id + random.randint(0, max_range)
        tmp.append(q_id)
    return tmp






