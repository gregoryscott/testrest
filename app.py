from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/api/sum_matrix', methods=['POST'])
def sum_matrix():
    try:
        # Get the JSON data from the request
        data = request.json

        # Ensure the data contains a 'matrix' key
        if 'matrix' not in data:
            return jsonify(error="Missing 'matrix' key in JSON data"), 400
        
        # Ensure the 'matrix' key contains a list of lists
        matrix = data['matrix']
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            return jsonify(error="'matrix' must be a list of lists"), 400
        
        # Convert the list of lists to a NumPy array
        np_matrix = np.array(matrix)
        
        # Sum the elements of the matrix
        result_sum = np.sum(np_matrix).item()

        # Return the result as a JSON response
        return jsonify(result_sum=result_sum)
    
    except Exception as e:
        # Handle any other exceptions and return an error message
        return jsonify(error=str(e)), 500
