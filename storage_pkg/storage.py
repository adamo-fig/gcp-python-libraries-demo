from google.cloud import storage
from google.cloud.storage import Client

# Cambia aqui por el nombre de tu bucket
# my_bucket = "qwiklabs-gcp-70a66879a9535fca"
my_bucket = "buho-platform.appspot.com"



# Obtiene un cliente de conexión
def get_client() -> Client:
    return storage.Client()

# Muestra los buckets del proyecto actual


def listarBuckets():
    client = get_client()
    buckets = client.list_buckets()
    print(list(buckets))


def crearBucket():
    try:
        client = get_client()
        client.create_bucket(my_bucket)
    except Exception as ex:
        print("Ocurrio un error probablemente ya existe el bucket", ex)


def subirArchivos():
    client = get_client()
    bucket = client.get_bucket(my_bucket)
    bucket.blob("archivito.txt").upload_from_filename("./archivo.txt")
    with open("archivo.txt", "rb") as my_file:
        bucket.blob("archivito2.txt").upload_from_file(my_file)


def subirConTexto():
    client = get_client()
    bucket = client.get_bucket(my_bucket)
    bucket.blob("texto.txt").upload_from_string("Adamó Figueroa")
    bucket.blob("dir/texto.txt").upload_from_string("Adamó Figueroa")
    bucket.blob("dir/dir2/texto.txt").upload_from_string("Adamó Figueroa")


def subirVarios():
    client = get_client()
    bucket = client.get_bucket(my_bucket)
    dir = ""

    for i in range(30):
        dir = dir + "carpeta" + str(i) + "/"
        archivo = "archivo" + str(i)
        bucket.blob(dir+archivo).upload_from_string("Lorem Ipsum Dolorem")


def subirArchivoWeb(file):
    client = get_client()

    bucket = client.get_bucket(my_bucket)
    bucket.blob(file.filename).upload_from_file(file)


def consultarArchivos(prefix, delimiter):
    client = get_client()
    bucket = client.get_bucket(my_bucket)
    files = bucket.list_blobs(prefix=prefix, delimiter=delimiter)

    compFiles = [{"name": file.name, "selfLink": file.self_link}
                 for file in files]

    return {"items": compFiles, "prefixes": list(files.prefixes)}


# listarBuckets()
# crearBucket()
# subirVarios()
