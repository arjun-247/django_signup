from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    p='davis'
    return render_template('home.html',n=p)

@app.route('/pgm')
def index():
    x=[1,2,3,4,5]
    y={'name':'Arjun','age':'21','place':'ekm'}
    return render_template('pgm2.html',n=x,s=y)

@app.route('/index')
def hello():
    return 'Hello flask'

if __name__ == '__main__':
    app.run(debug=True,port=8001)