from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    logged_text = ""

    if request.method == "POST":
        text = request.form.get("text", "")

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("logs.txt", "a") as f:
            f.write(f"[{time}] {text}\n")

        logged_text = text

    try:
        with open("logs.txt", "r") as f:
            logs = f.read()
    except:
        logs = ""

    return render_template("index.html", logged_text=logged_text, logs=logs)

@app.route("/clear", methods=["POST"])
def clear():
    open("logs.txt", "w").close()
    return index()

if __name__ == "__main__":
    app.run(debug=True)