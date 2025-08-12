"""
This module provides route handling for all routes accessible within the app

It includes functions for 
- extracting emotion data from responses
- rendering the front-end side of the application
- executing a connection to the localhost:5000 server
"""
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    This function extracts scores of emotion context data when a submission is executed
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    message_1 = f"{anger}, 'disgust': {disgust},'fear': {fear}, 'joy': {joy},"
    message_2 = f" and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return "For the given statement, the system response is 'anger': " + message_1 + message_2

@app.route("/")
def render_index_page():
    """
    This function allows users to interact with the app when using the main home directory
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
