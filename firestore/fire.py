from google.cloud import firestore
from google.cloud.firestore import DocumentReference

# db.collection("usuarios").add({"nombre":"Adamo", "edad":25 })
def monitoreoDatos():
    prueba: DocumentReference
    
    def mostrarCambios(snap, changes, read_time):
        print("tenemos cambios",list(snap))
        for doc in snap:
            print(doc.id)
            print(doc.data())
        
    
    db = firestore.Client()
    db.collection("usuarios").on_snapshot(mostrarCambios)

