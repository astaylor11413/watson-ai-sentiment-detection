import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
    formatted_response = json.loads(str(response.text))
    anger = formatted_response['emotionPredections']['emotion']['anger']
    disgust = formatted_response['emotionPredections']['emotion']['disgust']
    fear = formatted_response['emotionPredections']['emotion']['fear']
    joy = formatted_response['emotionPredections']['emotion']['joy']
    sadness = formatted_response['emotionPredections']['emotion']['sadness']
    dominant_emotion = max(anger,disgust,fear,joy,sadness)
    return {'anger':anger,
            'disgust':disgust,
           'fear':fear,
            'joy':joy,
            'sadness':sadness, 
            'dominant_emotion':dominant_emotion} 
    
    