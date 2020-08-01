
from flask import Flask, request
from modules.text_processor import text_pipeline
from modules.create_event import create_log_file
from os import remove
import base64

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        img_data = request.form['img_string']

        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(img_data))

        create_log_file(text_pipeline())

        deciphered_string = ""
        with open("event_log_file.txt", "r") as txt:
            deciphered_string = txt.read()

        remove("imageToSave.png")
        remove("tessaract_text.txt")

        print(deciphered_string)
        return deciphered_string
    else:
        return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
