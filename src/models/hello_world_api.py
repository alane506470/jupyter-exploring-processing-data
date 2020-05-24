
from flask import Flask,request

app = Flask(__name__)

@app.route('/api',methods=['POST'])
def say_hell():
    return "hello World"
if __name__ == '__main__':
    app.run()
