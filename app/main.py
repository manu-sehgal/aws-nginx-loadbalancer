from flask import Flask
import os
import socket

app = Flask(__name__)

SERVER_NAME = os.getenv("SERVER_NAME", "Unknown Server")


@app.route("/")
def home():
    return {
        "message": "Hello from backend!",
        "server": SERVER_NAME,
        "hostname": socket.gethostname()
    }


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)