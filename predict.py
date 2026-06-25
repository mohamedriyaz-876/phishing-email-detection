import pickle

model = pickle.load(open("models/phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

while True:
    email = input("\nEnter email text: ")

    email_vector = vectorizer.transform([email])

    result = model.predict(email_vector)

    if result[0] == 1:
        print("⚠️ PHISHING EMAIL")
    else:
        print("✅ SAFE EMAIL")
