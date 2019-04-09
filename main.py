def holaMundo(request):
    return "Hola mundo"
    
def testQueryParam(resquest):
    id = resquest.args.get("id")
    name = resquest.args.get("name")
    return "tu id es " + id + " tu nombre es " + name

# gcloud functions deploy holaAdamo2 --runtime python37 --trigger-http