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


# gcloud functions deploy holaAdamo2 --runtime python37 --trigger-http