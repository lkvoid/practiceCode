from flask import Flask

app = Flask(__name__)

@app.route('/main.html')
def hello_world():

    return '/main.html'

if __name__ == '__main__':
    app.run()
