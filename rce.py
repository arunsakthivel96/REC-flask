from flask import Flask, redirect, url_for, request,render_template
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route('/',methods=['POST','GET'])
def index(userName=None):
    if request.method == 'POST':
        data = request.form['name']
        userName = Jinja2.from_string(data).render()
        
        return render_template('index.html',name=userName)
    else:
        return render_template('index.html',name=userName)

if __name__ == '__main__':
   app.run("0.0.0.0",4444,debug=True)