import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('/etc/secrets/my-secrets-config', 'r') as secret_file:
            secret_value = secret_file.read().strip()
    except FileNotFoundError:
        secret_value = "Secret file not found."

    text = "{}<br><br>Here's my secret: {}".format(
        os.environ.get('APP_MESSAGE', 'Hello, World!'),
        secret_value
    )
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)