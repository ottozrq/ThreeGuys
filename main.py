from flask import Flask, jsonify, render_template
from flask_assets import Environment
import dataOperations as dao

app = Flask(__name__)
assets = Environment(app)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/shared/<uid>")
def shared(uid=""):
    return render_template('index.html', uid)


@app.route("/get/<uid>")
def get(uid):
    json = dao.get(uid)
    if "error" in json:
        return jsonify(json)
    else:
        return jsonify(eqtls=[e.serialize() for e in json])


@app.route("/submit", methods=['POST'])
def submit(data, uid):
    json = dao.submit(data, uid)
    return jsonify(json)


@app.route("/save", methods=['POST'])
def save(data):
    json = dao.save(data)
    return jsonify(json)


@app.route("/backend")
def backend():
    return 'backend'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
