from flask import Flask, render_template, request

app = Flask(__name__)

# Simple Disease Dictionary
disease_data = {

    "fever cough headache": {
        "disease": "Flu",
        "medicine": "Paracetamol",
        "diet": "Drink warm fluids",
        "workout": "Take rest"
    },

    "itching skin_rash": {
        "disease": "Fungal Infection",
        "medicine": "Antifungal cream",
        "diet": "Avoid oily food",
        "workout": "Light walking"
    },

    "headache nausea vomiting": {
        "disease": "Migraine",
        "medicine": "Pain reliever",
        "diet": "Drink water",
        "workout": "Rest"
    },

    "fever chills sweating": {
        "disease": "Malaria",
        "medicine": "Antimalarial drugs",
        "diet": "Drink fluids",
        "workout": "Bed rest"
    },

    "fever cough breathing_problem": {
        "disease": "COVID-19",
        "medicine": "Consult doctor",
        "diet": "Healthy diet",
        "workout": "Isolation and rest"
    },

    "stomach_pain diarrhea vomiting": {
        "disease": "Food Poisoning",
        "medicine": "ORS solution",
        "diet": "Light food",
        "workout": "Rest"
    },

    "fever headache joint_pain": {
        "disease": "Dengue",
        "medicine": "Paracetamol",
        "diet": "Papaya leaf juice",
        "workout": "Rest"
    },

    "sneezing runny_nose cough": {
        "disease": "Common Cold",
        "medicine": "Cold tablets",
        "diet": "Warm soup",
        "workout": "Rest"
    },

    "chest_pain shortness_of_breath": {
        "disease": "Heart Problem",
        "medicine": "Consult doctor immediately",
        "diet": "Low fat diet",
        "workout": "Avoid exercise"
    },

    "thirst fatigue frequent_urination": {
        "disease": "Diabetes",
        "medicine": "Insulin / Tablets",
        "diet": "Low sugar diet",
        "workout": "Walking"
    },

    "weight_loss fatigue weakness": {
        "disease": "Thyroid",
        "medicine": "Thyroid medication",
        "diet": "Balanced diet",
        "workout": "Yoga"
    },

    "fever sore_throat cough": {
        "disease": "Throat Infection",
        "medicine": "Antibiotics",
        "diet": "Warm fluids",
        "workout": "Rest"
    },

    "back_pain stiffness": {
        "disease": "Back Pain",
        "medicine": "Pain relief gel",
        "diet": "Healthy diet",
        "workout": "Stretching"
    },

    "eye_redness itching": {
        "disease": "Eye Infection",
        "medicine": "Eye drops",
        "diet": "Vitamin A foods",
        "workout": "Rest eyes"
    },

    "fever body_pain fatigue": {
        "disease": "Viral Fever",
        "medicine": "Paracetamol",
        "diet": "Drink fluids",
        "workout": "Rest"
    }

}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():

    symptoms = request.form['symptoms'].lower()

    result = {
        "disease": "Not Found",
        "medicine": "Consult Doctor",
        "diet": "Healthy Diet",
        "workout": "Rest"
    }

    for key in disease_data:
        if all(symptom in symptoms for symptom in key.split()):
            result = disease_data[key]
            break

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)