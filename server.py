from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # 从网页请求中获取待分析的文本 (键名为 'textToAnalyze')
    text_to_analyze = request.args.get('textToAnalyze')

    # 调用之前编写的函数进行情绪检测
    response = emotion_detector(text_to_analyze)

    # 提取结果中的各情绪得分和主导情绪
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # 按照任务要求的格式构造返回字符串
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    # 渲染主页
    return render_template('index.html')

if __name__ == "__main__":
    # 在 5000 端口启动应用
    app.run(host="0.0.0.0", port=5000)