from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# app.run(debug=True)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emote():
    text_to_analyse = request.args.get('textToAnalyse')
    
    return text_to_analyse

    # response = emotion_detector(text_to_analyse)

    # s = "For the given statement, the system response is 'anger': " + str(response['anger'])

    # return response

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
