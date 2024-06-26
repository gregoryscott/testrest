from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    matrix = np.array(data['matrix'])
    # Sum the elements of the matrix
    result_sum = np.sum(matrix)
    return jsonify(result_sum=result_sum)
