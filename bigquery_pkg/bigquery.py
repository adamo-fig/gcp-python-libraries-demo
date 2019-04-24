def insertarDatosBQ():
    from google.cloud import bigquery

    clientBQ = bigquery.Client()

    SCHEMA = [ 
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("age", "INTEGER")
    ]

    try:
        clientBQ.create_dataset("adamo")
    except:
        print("probablemente ya existe el data set ")

    try:
        tabla =bigquery.Table("qwiklabs-gcp-2f2c53419aada66c.adamo.datosAdamo2",schema=SCHEMA)
        clientBQ.create_table(tabla)
    except:
        print("tal vez ya existe")

    tabla = clientBQ.get_table("qwiklabs-gcp-2f2c53419aada66c.adamo.datosAdamo2")
    
    tupla1 = [("adamo",25), ("jordan", 26)]
    dict1 = [{ "name":"adamo2" , "age": 30},{ "name":"jordan2" , "age": 30} ]
    
    clientBQ.insert_rows(tabla, dict1)

# insertarDatosBQ()