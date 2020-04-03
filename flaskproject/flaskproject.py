from flask import Flask,render_template
from data import About

app =Flask(__name__)

About=About()

@app.route('/')

def index():
	return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html',about=About)



if __name__=="__main__":
    app.run(debug=True)
