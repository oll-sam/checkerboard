from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html", column=8, row=8)

@app.route('/<int:num>')
def number(num):
    return render_template ("index.html", column=8, row=num)

@app.route('/<int:num>/<int:num1>')
def number1(num1,num):
    return render_template("index.html", column=num1, row=num)

@app.route('/<int:num>/<int:num1>/<color1>')
def color(num, num1, color1):
    return render_template("index.html", column=num1, row=num, color1=color1)

@app.route('/<int:num>/<int:num1>/<color1>/<color2>')
def color1(num, num1, color1, color2):
    return render_template("index.html", column=num1, row=num, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)