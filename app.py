import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "hello"


if __name__ == "__main__":
    app.run()
