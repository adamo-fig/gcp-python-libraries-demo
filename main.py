from firestore_pkg import firestore
from storage_pkg import storage
from flask import Flask, jsonify, request
from flask_cors import CORS

from pubsub_pkg import pubsub 
import main

app = Flask(__name__)
CORS(app)


@app.route("/")
def holaMundo():
    return holaMundo(request)


@app.route("/testQueryParam")
def testQueryParam():
    return testQueryParam(request)


@app.route("/json")
def json():
    dictionario = {"nombre": "Adamo", "edad": 25}
    return jsonify(dictionario)


@app.route("/jsonpost", methods=["POST"])
def jsonPost():
    data = request.json
    print(data["valor"])
    print(data["valor2"])
    return "Ok ..."


@app.route("/uploadFile", methods=["POST"])
def uploadFile():
    file = request.files["archivo"]
    print(type(file), file.filename)
    storage.subirArchivoWeb(file)
    return jsonify({"response": "ok"})


@app.route("/consultarArchivos")
def consultarArchivos():
    return consultarArchivos(request)


@app.route("/monitorData")
def iniciarMonitoreo():
    firestore.monitoreoDatos()

@app.route("/iniciarPubSub")
def iniciarPubSub():
    pubsub.sub("buho-platform","mySub1")


#### Funciones 
# python diferencia funciones por parametro
# gcloud functions deploy holaAdamo2 --runtime python37 --trigger-http

def holaMundo(request):
    return "Hola mundo"
    
def testQueryParam(resquest):
    id = resquest.args.get("id")
    name = resquest.args.get("name")
    return "tu id es " + id + " tu nombre es " + name

def consultarArchivos(request):
    from storage_pkg import storage
    from flask import jsonify


    prefix = request.args.get("prefix")
    delimiter = request.args.get("delimiter")
    print("Parametros -> prefix:", prefix,  " delimitador:",  delimiter)
    result_files = storage.consultarArchivos(prefix, delimiter)
    return jsonify(result_files)

# No queremos que se ejecute en la nube, lo tiene que ejecutar un servidor como Gunicorn
if __name__ == '__main__':
    app.run()

