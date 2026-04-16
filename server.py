"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# 初始化 Flask 应用
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text provided by the user and returns the emotion scores
    and the dominant emotion.
    """
    # 从请求参数中获取文本
    text_to_analyze = request.args.get('textToAnalyze')

    # 调用情绪检测函数
    response = emotion_detector(text_to_analyze)

    # 提取情绪分数和主导情绪
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # 处理空输入（Task 7 的逻辑）
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # 返回格式化后的字符串
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask dev server.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    