from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# 1. Load the pre-trained ML models safely
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
models_dir = os.path.join(BASE_DIR, 'models')

diabetes_model = pickle.load(open(os.path.join(models_dir, 'diabetes_model.pkl'), 'rb'))
heart_model = pickle.load(open(os.path.join(models_dir, 'heart_model.pkl'), 'rb'))
ckd_model = pickle.load(open(os.path.join(models_dir, 'ckd_model.pkl'), 'rb'))

# PAGE ROUTES 
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/diabetes')
def diabetes_page():
    return render_template('diabetes_form.html')

@app.route('/heart')
def heart_page():
    return render_template('heart_form.html')

@app.route('/kidney')
def kidney_page():
    return render_template('kidney_form.html')

# PREDICTION ROUTES 

# 1. Diabetes Prediction
@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    features = [
        float(request.form['pregnancies']),
        float(request.form['glucose']),
        float(request.form['bloodpressure']),
        float(request.form['skinthickness']),
        float(request.form['insulin']),
        float(request.form['bmi']),
        float(request.form['dpf']),
        float(request.form['age'])
    ]
    prediction = diabetes_model.predict([features])[0]
    result_text = "High Risk of Diabetes" if prediction == 1 else "Low Risk of Diabetes"
    return render_template('result.html', result=result_text, module="Diabetes Module")

# 2. Heart Disease Prediction
@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    features = [
        float(request.form['cp']),
        float(request.form['chol']),
        float(request.form['thalch']),
        float(request.form['age']),
        float(request.form['oldpeak']),
        float(request.form['exang'])
    ]
    prediction = heart_model.predict([features])[0]
    result_text = "High Risk of Cardiovascular Disease" if prediction == 1 else "Low Risk of Cardiovascular Disease"
    return render_template('result.html', result=result_text, module="Cardiovascular Module")

# 3. CKD Prediction
@app.route('/predict_kidney', methods=['POST'])
def predict_kidney():
    features = [
        float(request.form['sg']),
        float(request.form['hemo']),
        float(request.form['sc']),
        float(request.form['pcv']),
        float(request.form['al']),
        float(request.form['bgr'])
    ]
    prediction = ckd_model.predict([features])[0]
    # THE FIX: Changed 'prediction == 1' to 'prediction == 0' so it matches the AI's math!
    result_text = "High Risk of Chronic Kidney Disease" if prediction == 0 else "Low Risk of Chronic Kidney Disease"
    return render_template('result.html', result=result_text, module="Renal Function Module")

if __name__ == '__main__':
    app.run(debug=True)