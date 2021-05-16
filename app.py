from flask import Flask

from PEPPSaF.IPDetector import IPDetector

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {"wlan": IPDetector.detect('')}


if __name__ == '__main__':
    app.run()
