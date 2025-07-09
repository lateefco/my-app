import os
from flask import Flask
import configparser
app = Flask(__name__)

@app.route('/')
def index():
    config = configparser.ConfigParser()
    file_path = os.path.abspath('config.ini')
    config.read(file_path)
    try:
            secret_value = config['AWS']['aws_secret_access_key']
            print(f"Successfully read secret key: {secret_value}")
    except KeyError:
        print("error cannot read key")

    text = "{}<br><br>Here's my secret: {}".format(
        os.environ.get('APP_MESSAGE', 'Hello, World!'),
        secret_value
    )
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)