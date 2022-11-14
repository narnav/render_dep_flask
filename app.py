from flask import Flask
app = Flask(__name__)

ar=[{"name":"aviel"},{"name":"jacov"}]

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/dt')
def dt():
    return ar


if __name__ == '__main__':
    app.run(debug=True)
