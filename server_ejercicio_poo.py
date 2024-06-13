from fit_db import get_db
from class_ejercicio import ejercicio


def insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit (ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)     VALUES ( ?, ?, ?, ? ,?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad])
    db.commit()
    return True

def update_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit SET ejercicio = ?, repeticiones = ?, tiempo= ?, peso= ?, fortalece= ?, number_pages= ?, press= ? WHERE ID = ?"
    cursor.execute(statement, [ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad, ID])
    db.commit()
    return True


def delete_ejercicio(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    db.commit()
    return True


def get_by_id(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    single_ejercicio = cursor.fetchone()
    ID = single_ejercicio[0]
    ejercicio = single_ejercicio[1]
    repeticiones = single_ejercicio[2]
    tiempo = single_ejercicio[3]
    peso = single_ejercicio[4]
    fortalece = single_ejercicio[5]
    serie = single_ejercicio[6]
    dificultad = single_ejercicio[7]
    ejercicio = ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
    return ejercicio.serialize_details()


def get_ejercicio():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad FROM fit"
    cursor.execute(query)
    ejercicio_list = cursor.fetchall()
    list_of_ejercicios=[]
    for ejercicio in list_of_ejercicios:
        ID = ejercicio[0]
        ejercicio = ejercicio[1]
        repeticiones = ejercicio[2]
        tiempo = ejercicio[3]
        peso = ejercicio[4]
        fortalece = ejercicio[5]
        serie = ejercicio[6]
        dificultad = ejercicio[7]
        ejercicio_to_add = ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
        list_of_ejercicios.append(ejercicio_to_add)
    return list_of_ejercicios