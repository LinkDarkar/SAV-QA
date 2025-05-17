import os
import json
from flask import Flask, request, jsonify, redirect, send_from_directory
import tempfile
import shutil
import requests
import pydrive2

from manage import TEMP_FOLDER, JSON_FILE_PATH











# Definir una ruta para manejar solicitudes POST y recibir un JSON
@app.route('/redirect', methods=['POST'])
def redirectToLink():
    # Obtener el JSON enviado en la solicitud
    data = request.get_json()

    # Verificar si el JSON contiene un parámetro 'parametro'
    if 'Link' in data:
        link = data['Link']
        return redirect(link)
    else:
        return jsonify({"error": "No se encontró el parámetro"}), 400


"""
    Intento de acceder a solo el primer elemento del json, se me olvidó por qué estaba haciendo esto
    pero hey, ahora se sabe.
    Eso si, el json que tenemos es un diccionario. Así que tuve que hacer este workaround feo
    para no tener que poner el nombre del elemento si o si

    ... ya me acordé, era para que, si al final hacíamos lo de tener un json dentro de la carpeta que contenga
    los IDs de los archivos que están dentro de esta, lo ideal sería que estos tuviesen un nombre para que el que
    pusiera los jsons ahí no se perdiera tanto. Y así fue como nacio esta basura de acá
"""
@app.route('/jsonReadTest', methods=['POST'])
def jsonReadTest():
    # Obtener el JSON enviado en la solicitud
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)  # Cargar el contenido del archivo JSON

    print(len(data))
    if len(data) > 1:
        return redirect(list(data.values())[0])


@app.route('/redirect/emailTest/<email>', methods=['POST'])
def redirectToCertainEmail(email):
    print(f"HI, {email}")

    if email == "admin":
        return redirectToFolder()
    else:
        return redirectPage()

