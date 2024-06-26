from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/api/sum_matrix', methods=['POST'])
def sum_matrix():
    data = request.json
    matrix = np.array(data['matrix'])
    # Sum the elements of the matrix
    result_sum = np.sum(matrix)
    return jsonify(result_sum=result_sum)
