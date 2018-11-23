from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_assets import Environment
from flask_cors import cross_origin
import dataOperations as dao

app = Flask(__name__)
assets = Environment(app)
app.debug = True


@app.route("/", defaults={'uid': None})
@app.route("/<uid>")
def index(uid=""):
    return render_template('index.html', uid=uid)


@app.route("/get/<uid>")
def get(uid):
    json = dao.get(uid)
    if "error" in json:
        return jsonify(json), 404
    else:
        return jsonify(eqtls=[e.serialize() for e in json])


@app.route("/submit/", defaults={'uid': None}, methods=['POST'])
@app.route("/submit/<uid>", methods=['POST'])
@cross_origin()
def submit(uid=""):
    data = request.json
    json = dao.submit(data, uid)
    return jsonify(json)


@app.route("/save/", defaults={'uid': None}, methods=['POST'])
@app.route("/save/<uid>", methods=['POST'])
@cross_origin()
def save(uid=""):
    data = request.json
    print data
    json = dao.save(data, uid)
    return jsonify(json)


@app.route("/backend")
def backend():
    json = dao.getall()
    data = [e.to_json_obj() for e in json]
    return render_template('backend.html', data=data)


@app.route('/assets/data/data.json')
def send_file():
    return send_from_directory('assets/data/', 'data.json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
