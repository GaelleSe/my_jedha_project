import joblib

from flask import Flask, request, json, jsonify,render_template
from werkzeug.exceptions import HTTPException

MODEL_PATH = "model.joblib"

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    print("1")
    # Check if request has a JSON content
    if request.json:
        print (request.json)
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            print("2")
            # Load model
            classifier = joblib.load("model.joblib")
            # Predict
            prediction = classifier.predict(req["input"])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = str(prediction[0])
            return jsonify({"predict": prediction}), 200
        
    return jsonify({"msg": "Error: not a JSON or no email key in your request"})


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  

