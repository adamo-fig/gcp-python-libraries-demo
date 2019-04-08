from google.cloud import storage 
# En este nivel tenemos todos los objetos

client = storage.Client()

print("________Iniciando con cloud storage")
my_bucket = "qwiklabs-gcp-70a66879a9535fca"

def crearBucket():
    try:
        client.create_bucket(my_bucket)
    except Exception as ex:
        print("Ocurrio un error probablemente ya existe el bucket", ex)

def subirArchivos():
    bucket = client.get_bucket(my_bucket)

    bucket.blob("archivito.txt").upload_from_filename("./archivo.txt")

    with open ("archivo.txt", "rb") as my_file:
        bucket.blob("archivito2.txt").upload_from_file(my_file)


def subirConTexto():
    bucket = client.get_bucket(my_bucket)
    bucket.blob("texto.txt").upload_from_string("Adamó Figueroa")
    bucket.blob("dir/texto.txt").upload_from_string("Adamó Figueroa")
    bucket.blob("dir/dir2/texto.txt").upload_from_string("Adamó Figueroa")


def subirVarios():
    bucket = client.get_bucket(my_bucket)
    dir = ""

    for i in range(30):
        dir = dir + "carpeta"+ str(i) + "/"
        archivo = "archivo" + str(i)
        bucket.blob(dir+archivo).upload_from_string("Lorem Ipsum Dolorem")

def subirArchivoWeb(file):
        bucket = client.get_bucket(my_bucket)
        bucket.blob(file.filename).upload_from_file(file)

def consultarArchivos(prefix,delimiter):
        bucket = client.get_bucket(my_bucket)
        files = bucket.list_blobs(prefix=prefix, delimiter=delimiter)

        compFiles = [ {"name":file.name , "selfLink": file.self_link} for file in files]

        print('Prefixes:')
        for prefix in files.prefixes:
                print(prefix)
                
        return {"items":compFiles , "prefixes": list(files.prefixes) }


# consultarArchivos("","/")
# crearBucket()
# subirVarios()

