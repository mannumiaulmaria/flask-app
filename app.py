from flask import Flask,render_template
from database import get_data


app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html', data=data)

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/login',)
def login():
    return render_template('login.html')




if __name__ =="main":
  app.run()

