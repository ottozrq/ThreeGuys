from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit")
def submit():
    return 'submit'

@app.route("/save")
def save():
    return 'save'

@app.route("/backend")
def backend():
    return 'backend'

if __name__ == "__main__":
    app.run(host='0.0.0.0')