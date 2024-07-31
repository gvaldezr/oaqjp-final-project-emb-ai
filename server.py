'''
Function to call emotion analyzer 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_analyzer():
    ''' Analyzer '''
    text_to_analyse = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyse)
    if res['dominant'] == 'none':
        return "Invalid text! Please try again!"
    formated_res = f"anger:{res['anger']}, disgust:{res['disgust']}, "
    formated_res += f"fear:{res['fear']}, joy:{res['joy']}, sadness:{res['sadness']} "
    res_dominant = f"The dominant emotion is {res['dominant']}"
    return f"For the given statement, the system response is {formated_res}. {res_dominant}"

@app.route("/")
def render_index_page():
    '''Render index '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
