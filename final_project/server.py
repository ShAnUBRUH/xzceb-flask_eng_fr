
from flask import Flask, render_template, request
from machinetranslation import translator
#import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def English_to_French():
    """ Translate text from english to french """
    text_to_translate = request.args.get('textToTranslate')
    return translator.English_to_French(text_to_translate)

@app.route("/frenchToEnglish")
def French_to_English():
    """ Transate text from french to english """
    text_to_translate = request.args.get('textToTranslate')
    return translator.French_to_English(text_to_translate)

@app.route("/")
def render_index_page():
    """ Route requests to index.html page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
