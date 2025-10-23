from flask import Flask

app = Flask(__name__)

# Root URL returns plain text
@app.route("/")
def hello():
    return "Hello from Cloud Run!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
