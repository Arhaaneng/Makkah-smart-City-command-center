
from flask import Flask, send_file
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return send_file(
        Path(__file__).with_name("alldone.html")
    )

if __name__ == "__main__":
    app.run(debug=True)
