from flask import Flask, render_template,request,jsonify
import numpy as np
import pickle

import flask

app = Flask(__name__)

model=pickle.load(open("modelAnn.pkl","rb"))

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/test-your-stress")
def question():
    return render_template('home.html')        

@app.route("/home")
def home1():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def predict():
    anxiety_level = int(request.form['anxiety'])
    self_esteem_vibe = int(request.form['self_esteem'])
    mental_health_history = int(request.form['mental_health'])
    depression_symptoms = int(request.form['depression'])
    headache_frequency = int(request.form['headache_frequency'])
    blood_pressure = int(request.form['blood_pressure'])
    sleep_quality = int(request.form['sleep_quality'])
    breathing_problem = int(request.form['breathing_problem'])
    noise_irritation = int(request.form['noise_irritation'])
    living_conditions = int(request.form['living_conditions'])
    safety_feeling = int(request.form['safety_feeling'])
    basic_needs_fulfillment = int(request.form['basic_needs_fulfillment'])
    academic_progress = int(request.form['academic_progress'])
    study_load = int(request.form['study_load'])
    teacher_student_relationship = int(request.form['teacher_student_relationship'])
    future_career = int(request.form['future_career'])
    social_support = int(request.form['social_support'])
    peer_pressure = int(request.form['peer_pressure'])
    extracurricular_involvement = int(request.form['extracurricular_involvement'])
    bullying_frequency = int(request.form['bullying_frequency'])
    inputData=np.array([[anxiety_level, self_esteem_vibe, mental_health_history, depression_symptoms, headache_frequency, blood_pressure, sleep_quality, breathing_problem, noise_irritation, living_conditions, safety_feeling, basic_needs_fulfillment, academic_progress, study_load, teacher_student_relationship, future_career, social_support, peer_pressure, extracurricular_involvement, bullying_frequency]])
    pred = model.predict(inputData)
    prediction = np.argmax(pred, axis=1)  
    print(anxiety_level, self_esteem_vibe, mental_health_history, depression_symptoms, headache_frequency, blood_pressure, sleep_quality, breathing_problem, noise_irritation, living_conditions, safety_feeling, basic_needs_fulfillment, academic_progress, study_load, teacher_student_relationship, future_career, social_support, peer_pressure, extracurricular_involvement, bullying_frequency)
    
    if prediction[0] == 0:
        predict1 = "No stress"
    elif prediction[0] == 1:
        predict1 = "Stress"
    else:
        predict1 = "High Stress"   
    anxiety_level = important_attributes(anxiety_level, 11.06)
    self_esteem_vibe = important_attributes(self_esteem_vibe, 17.78)
    mental_health_history = important_attributes(mental_health_history, 0.49)
    depression_symptoms = important_attributes(depression_symptoms, 12.56)
    headache_frequency = important_attributes(headache_frequency, 2.51)
    blood_pressure = important_attributes(blood_pressure, 2.18)
    sleep_quality = important_attributes(sleep_quality, 2.66)
    breathing_problem = important_attributes(breathing_problem, 2.75)
    noise_irritation = important_attributes(noise_irritation, 2.65)
    living_conditions = important_attributes(living_conditions, 2.52)
    safety_feeling = important_attributes(safety_feeling, 2.74)
    basic_needs_fulfillment = important_attributes(basic_needs_fulfillment, 2.77)
    academic_progress = important_attributes(academic_progress, 2.77)
    study_load = important_attributes(study_load, 2.62)
    teacher_student_relationship = important_attributes(teacher_student_relationship, 2.65)
    future_career = important_attributes(future_career, 2.65)
    social_support = important_attributes(social_support, 1.88)
    peer_pressure = important_attributes(peer_pressure, 2.73)
    extracurricular_involvement = important_attributes(extracurricular_involvement, 2.77)
    bullying_frequency = important_attributes(bullying_frequency, 2.62)
    print(anxiety_level, self_esteem_vibe, mental_health_history, depression_symptoms, headache_frequency, blood_pressure, sleep_quality, breathing_problem, noise_irritation, living_conditions, safety_feeling, basic_needs_fulfillment, academic_progress, study_load, teacher_student_relationship, future_career, social_support, peer_pressure, extracurricular_involvement, bullying_frequency)
    return render_template('predict.html', prediction1=predict1, anxiety_level=anxiety_level, self_esteem_vibe=self_esteem_vibe, mental_health_history=mental_health_history, depression_symptoms=depression_symptoms, headache_frequency=headache_frequency, blood_pressure=blood_pressure, sleep_quality=sleep_quality, breathing_problem=breathing_problem, noise_irritation=noise_irritation, living_conditions=living_conditions, safety_feeling=safety_feeling, basic_needs_fulfillment=basic_needs_fulfillment, academic_progress=academic_progress, study_load=study_load, teacher_student_relationship=teacher_student_relationship, future_career=future_career, social_support=social_support, peer_pressure=peer_pressure, extracurricular_involvement=extracurricular_involvement, bullying_frequency=bullying_frequency)

    # return render_template('predict.html', prediction1 = predict1,anxiety_level, self_esteem_vibe, mental_health_history, depression_symptoms, headache_frequency, blood_pressure, sleep_quality, breathing_problem, noise_irritation, living_conditions, safety_feeling, basic_needs_fulfillment, academic_progress, study_load, teacher_student_relationship, future_career, social_support, peer_pressure, extracurricular_involvement, bullying_frequency)
def important_attributes(attribute,mean):
    if(attribute<mean):
        return 1
    elif(attribute>mean):
        return 2
    else:
        return 0