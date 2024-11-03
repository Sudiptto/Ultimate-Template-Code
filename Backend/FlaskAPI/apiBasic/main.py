from flask import Flask, request, jsonify
from flask_cors import CORS

# initialize the flask app with Cors
app = Flask(__name__)
CORS(app)

# Simple Hello World route
@app.route("/getHelloWorld", methods=["GET"])
def getHelloWorld():
    return jsonify({"message": "Hello World!"}) 

# Run the app
if __name__ == "__main__":
    app.run(debug=True)