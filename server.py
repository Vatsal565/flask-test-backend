from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello World!",
        'team': ['Vatsal', 'Miten', 'Laskhit']
    })


if __name__ == "__main__":
    app.run()