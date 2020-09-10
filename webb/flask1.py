from flask import Flask, render_template,request,redirect,url_for
import json
from difflib import get_close_matches
from dicstu import dicty


data = json.load(open("data.json"))

app = Flask(__name__)

@app.route('/')
def home():
        return render_template("home.html")
    

@app.route('/result.html',methods=['POST','GET'])
def display():
    if request.method == 'POST':
      word = request.form['word']
      output=dicty(word)
      return render_template("home.html",word=word,result=output)
    
        
if __name__ == "__main__":
    app.run(debug=True)

