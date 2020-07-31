from flask import Flask
import requests
from os import getenv


app = Flask(__name__)


@app.route('/')
def hello_world():
    print(getenv('PRIVATE_ADDRESS') + getenv('PRIVATE_PORT') + '/private')
    data = requests.get('http://' + getenv('PRIVATE_ADDRESS') + ':' + getenv('PRIVATE_PORT') + '/private').text
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
