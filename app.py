from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("models/phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        email_text = request.form["email"]

        email_vector = vectorizer.transform([email_text])
        result = model.predict(email_vector)

        if result[0] == 1:
            prediction = "⚠️ Phishing Email"
        else:
            prediction = "✅ Safe Email"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
