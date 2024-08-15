'''
@Author : Shashi
@project : IBM Developing AI Applications with Python and Flask final project

'''

import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        formatted_response = json.loads(response.text)
        emotions_data = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions_data, key=emotions_data.get)

        output_data = {
            'anger': emotions_data['anger'],
            'disgust': emotions_data['disgust'],
            'fear': emotions_data['fear'],
            'joy': emotions_data['joy'],
            'sadness': emotions_data['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return output_data

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            print(f"HTTP error occurred: {http_err}")
            return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None