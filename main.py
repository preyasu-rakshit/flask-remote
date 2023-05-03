from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    print('stop')
    return 'hii'

@app.route('/forward')
def forw():
    print('forward')
    return 'hii'

@app.route('/backward')
def backw():
    print('backward')
    return 'hii'

@app.route('/left')
def left():
    print('left')
    return 'hii'

@app.route('/right')
def right():
    print('right')
    return 'hii'

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0',port=5000)