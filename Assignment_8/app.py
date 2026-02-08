from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    matches = []
    text = ""
    pattern = ""

    if request.method == "POST":
        text = request.form["text"]
        pattern = request.form["pattern"]

        try:
            matches = re.findall(pattern, text)
        except re.error:
            matches = ["Invalid Regular Expression"]

    return render_template("index.html", matches=matches, text=text, pattern=pattern)

if __name__ == "__main__":
    app.run(debug=True)
