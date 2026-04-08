from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy prediction function (replace with ML model)
def predict_tumor(image_path):
    return {
        "tumor_type": "Glioma",
        "confidence": 94,
        "area": "Left Frontal Lobe",
        "description": "This tumor appears due to abnormal growth",
        "cause": "Genetic mutation / radiation exposure",
        "suggestion": "Consult neurologist immediately"
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return redirect('/')

    file = request.files['file']
    if file.filename == '':
        return redirect('/')

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    result = predict_tumor(filepath)

    return render_template('result.html',
                           image_path=filepath,
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)

