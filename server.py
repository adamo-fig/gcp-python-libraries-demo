from flask import Flask, jsonify, request
from flask_cors import CORS

import main

app = Flask(__name__)
CORS(app)

import storage_pkg.storage as storage
import firestore_pkg.firestorep as firestore

@app.route("/")
def holaMundo():
    return main.holaMundo(request)

@app.route("/testQueryParam")
def testQueryParam():
    return main.testQueryParam(request)

@app.route("/json")
def json():
    dictionario = { "nombre":"Adamo" , "edad": 25}
    return jsonify(dictionario)

@app.route("/jsonpost" , methods=["POST"])
def jsonPost():
    data = request.json
    print(data["valor"])
    print(data["valor2"])
    return "Ok ..."

@app.route("/uploadFile", methods=["POST"])
def uploadFile():
    file = request.files["archivo"]
    print( type(file), file.filename)
    storage.subirArchivoWeb(file)
    return jsonify({"response":"ok"})

@app.route("/bucket")
def consultarArchivos():
    print(request.json)
    # data = request.json
    # storage.consultarArchivos(data["prefix"], data["delimiter"])
    return jsonify({"response":"ok"})


@app.route("/monitorData")
def iniciarMonitoreo():
    firestore.monitoreoDatos()



app.run()
