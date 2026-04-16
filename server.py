from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # 提取主导情绪
    dominant_emotion = response['dominant_emotion']

    # --- 新增错误处理逻辑 ---
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # -----------------------

    # 正常的返回逻辑
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    # 渲染主页
    return render_template('index.html')

if __name__ == "__main__":
    # 在 5000 端口启动应用
    app.run(host="0.0.0.0", port=5000)
