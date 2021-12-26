from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def url():
    return "test"

@app.route("/posts")
def postsurl():
    return "test"

if __name__ == "__main__":
    app.run(debug=True)