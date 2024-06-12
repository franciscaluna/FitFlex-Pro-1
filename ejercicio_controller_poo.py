from flask import Flask, jsonify, request
import server_ejercicio_poo
from fit_db import create_tables

app = Flask(__name__)


@app.route('/ejercicio', methods=["GET"])
def get_ejercicios():
    ejercicios = Untitled.get_books()
    ejercicios_list=[]
    for ejercicio in ejercicios:
        elem = ejercicios.serialize()
        ejercicios_list.append(elem)
    return jsonify(books_list)

@app.route("/ejercicio/create", methods=["POST"])
def insert_ejercicio():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    repeticiones =ejercicio_details["repeticiones"]
    tiempo = ejercicio_details["tiempo"]
    peso = ejercicio_details["peso"]
    fortalece = ejercicio_details["fortalece"]
    serie = ejercicio_details["serie"]
    dificultad = ejercicio_details ["dificultad"]
    result = server_ejercicio_poo.insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
    return jsonify(result)


@app.route("/ejercicio/modify", methods=["PUT"])
def update_ejercicio():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    repeticiones =ejercicio_details["repeticiones"]
    tiempo = ejercicio_details["tiempo"]
    peso = ejercicio_details["peso"]
    fortalece = ejercicio_details["fortalece"]
    serie = ejercicio_details["serie"]
    dificultad = ejercicio_details ["dificultad"]
    result = server_ejercicio_poo.update_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
    return jsonify(result)


@app.route("/ejercicio/eliminate/<ID>", methods=["DELETE"])
def delete_ejercicio(ID):
    result = server_ejercicio_poo.delete_book(ID)
    return jsonify(result)


@app.route("/ejercicio/<ID>", methods=["GET"])
def get_ejercicio_by_id(ID):
    book = server_ejercicio_poo.get_by_id(ID)
    return jsonify(book)

create_tables()

if __name__ == '__main__':
    app.run()