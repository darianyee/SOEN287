from flask import Flask, url_for, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/japan')
def japan():
    return render_template("Japan.html")

@app.route('/hawaii')
def hawaii():
    return render_template("Hawaii.html")

@app.route('/switzerland')
def switzerland():
    return render_template("Switzerland.html")


if __name__ == '__main__':
    app.run(debug=True)
