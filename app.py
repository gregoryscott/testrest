from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'Greg',
        'age': 123,
        'city': 'London'
    }
    return jsonify(data)
