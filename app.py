
from flask import Flask, render_template, request
from translate import Translator



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    lang=request.form['languages']
    translator= Translator(to_lang=lang)
    text = translator.translate(message)
    return render_template('index.html', prediction=text)    



if __name__ == '__main__':
	app.run(port=5002)


