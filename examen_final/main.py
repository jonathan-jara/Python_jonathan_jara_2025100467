from flask import Flask
from cliente import cliente  

app = Flask(__name__)


app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

