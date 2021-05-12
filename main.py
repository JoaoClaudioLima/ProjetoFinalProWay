from flask import Flask
from endpoints import init_api

app = Flask(__name__)
init_api(app)

if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")
