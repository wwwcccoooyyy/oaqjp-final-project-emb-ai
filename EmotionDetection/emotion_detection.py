import requests
import json

def emotion_detector(text_to_analyze):
    # API 配置
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # 发送请求
    response = requests.post(url, json = myobj, headers = header)
    
    # 1. 将响应文本转换为字典
    formatted_response = json.loads(response.text)
    
    # 2. 提取 'emotionPredictions' 里的情绪数据
    # 注意：Watson 返回的结构通常在 ['emotionPredictions'][0]['emotion'] 路径下
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 提取具体的 5 种情绪分数
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 3. 编写逻辑寻找得分最高的情绪 (Dominant Emotion)
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_list, key=emotion_list.get)
    
    # 4. 按照任务要求的格式构造返回的字典
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result