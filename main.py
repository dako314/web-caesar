from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "post">
        <label for "rot_number">Rotate by:</label>
        <input id = "rot_number" type = "text" name = "rot_number" value = "" autofocus/><br>
        <label>
            <textarea 
                name = "text_box">
                {text}
            </textarea>
        </label>
        <input type = "submit"/>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(text = 'Enter your text here')

@app.route("/", methods = ['POST'])
def encrpyt():
    rot = request.form['rot_number']
    text = request.form['text_box']
    rot = int(rot)
    content = rotate_string(text, rot)
    return form.format(text=content)

app.run()