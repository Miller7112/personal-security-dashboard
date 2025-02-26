from flask import Flask
from flask_cors import CORS
# import os

app = Flask(__name__)
CORS(app)

# Load configuration
app.config.from_pyfile('config.py')

# Load routes


@app
def home():
    return {"message": "Security Dashboard Backend Running"}


if __name__ == '__main__':
    app.run(debug=True)
