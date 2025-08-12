import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers= header)
    formatted_response = json.loads(str(response.text))
    emotions_array = formatted_response["emotionPredictions"]
    emotions_dict = emotions_array[0]
    anger = emotions_dict["emotion"]["anger"]
    disgust = emotions_dict["emotion"]["disgust"]
    fear = emotions_dict["emotion"]["fear"]
    joy = emotions_dict["emotion"]["joy"]
    sadness = emotions_dict["emotion"]["sadness"]
    max_score = max(anger, disgust, fear, joy, sadness)
    # To find the first key with the target value
    dominant_emotion = None
    for key, value in emotions_dict["emotion"].items():
        if value == max_score:
            dominant_emotion = key
            break  # Stop after finding the first match
    return {"anger" : anger, "disgust" : disgust,"fear" : fear,
            "joy" : joy,"sadness" : sadness,"dominant_emotion" : dominant_emotion}