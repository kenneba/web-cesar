from flask import Flask, request
from cesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
      <label> Rotate by
        <input type="text" name="rot" value="0" required/>
      </label>
        <textarea name="text" spellcheck="true" placeholder="Input a text to rotate" required>
        </textarea>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    text=request.form['text']
    encrypted_string = ""
    encrypted_string = rotate_string(text, rot)

    return '<h1>'+ encrypted_string + '</h1>'


app.run()
