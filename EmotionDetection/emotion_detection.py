import requests, json
def emotion_detector(text_to_analyse):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        return {'anger':'none', 'disgust':'none','fear':'none','joy':'none','sadness':'none','dominant':'none'}
    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions_data['anger']
    disgust_score = emotions_data['disgust']
    fear_score = emotions_data['fear']
    joy_score = emotions_data['joy']
    sadness_score = emotions_data['sadness']
    dominant = max(emotions_data.items(), key=lambda x: x[1])
    res = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score,
        'dominant' : dominant[0]
    }
    return res    
    #formatted_response = json.loads(response.text)
    #if response.status_code == 200:
    #    label = formatted_response['documentSentiment']['label']
    #    score = formatted_response['documentSentiment']['score']
    #elif response.status_code == 500:
    #    label = None
    #    score = None
    #return {'label': label, 'score': score}