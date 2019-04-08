# from google.cloud import firestore

try:

        from google.cloud import firestore
except Exception as e:
        print(e)

# db.collection("usuarios").add({"nombre":"Adamo", "edad":25 })

def monitoreoDatos():    
    def mostrarCambios(snap, changes, read_time):
        print("tenemos cambios",list(snap))
        for doc in snap:
            print(doc.id)
        #     print(doc)
        
    
    db = firestore.Client()
    db.collection("usuarios").on_snapshot(mostrarCambios)

