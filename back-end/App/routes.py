import os
import json
import requests
from flask import request, jsonify, redirect, send_from_directory
from GoogleDriveHandler import conectDrive

from App import app
from manage import JSON_USERTEST_PATH, JSON_FILE_PATH, TEMP_FOLDER, JSON_USERS_PATH, JSON_COMPANIES_PATH

@app.route('/list/results')
def listResults():
    # Llamada para listar los archivos en Google Drive
    conectDrive.list_drive_files()
    return 'Archivos listados en la consola!'

"""
    searchUserInDatabase y getDriveFolderID podrían ser una sola función
    aunque considerando que se tendrán que cambiar una vez que se tenga una
    base de datos pues puede ser que merezca la pena mantenerlas
    separadas para hacer los cambios más facilmente
"""
def searchUserInDatabase(username=None, company=None):
    with open(JSON_USERS_PATH, 'r') as file:
        usersData = json.load(file)
    
    for key, value in usersData.items():
        print(f"COMPARA: {value['name']} == {username} || {company} == {value['company']}")
        if username == value['name'] and company == value['company']:
            return getDriveFolderID(company)
    
    return False

def getDriveFolderID(company):
    with open(JSON_COMPANIES_PATH, 'r') as file:
        companiesData = json.load(file)
    
    for key, value in companiesData.items():
        print(f"COMPARA: {value['name']} == {company}")
        if company == value['name']:
            print(f"FOLDER ID: {value["folderID"]}")
            folderID = value["folderID"]
            return folderID
    
    return False
    
"""
    TODO gatillar búsqueda de las credenciales entregadas en el JSON
    que guarda credenciales de usuario.

    si lo encuentra, crear instancia de Session (???) y redirigir a la carpeta
    que le corresponde al usuario según la empresa a la que pertenece

    Entonces, busca si la empresa del usuario está y lo busca en la empresa.

    Una vez lo encuentre. Saca la carpeta que le corresponde a la empresa
    y la muestra en pantalla.

    
    Luego de implementarlo a medias sigo sin saber que hacer con Session.
"""
@app.route('/login', methods=['POST'])
def login():
    userData = request.get_json()

    with open(JSON_USERTEST_PATH, 'r') as file:
        data = json.load(file)

    username = userData['username']
    company = userData['company']

    print(f"recibido {username, company}")

    driveFolder = searchUserInDatabase(username, company)
    print(f"SE ENCONTRO EL ID {driveFolder}")

    if driveFolder == False:
        print("Falla")
        return None

    return redirectToFolder(driveFolder)

    

@app.route('/redirectToFolder', methods=['POST'])
def redirectToFolder(folderID):
    # Obtener el JSON enviado en la solicitud
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)  # Cargar el contenido del archivo JSON

    link = data['LinkToFolder'] + folderID
    return redirect(link)

"""
    # Verificar si el JSON contiene un parámetro 'parametro'
    if 'LinkToFolder' and 'FolderID' in data:
        link = data['LinkToFolder'] + data['FolderID']
        return redirect(link)
    else:
        return jsonify({"error": "No se encontró el parámetro"}), 400
"""

# Redirige al html puesto en el json al instante
@app.route('/redirect/html', methods=['POST'])
def redirectPage():
    # Obtener el JSON enviado en la solicitud
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)  # Cargar el contenido del archivo JSON

    # Verificar si el JSON contiene un parámetro 'LinkHtml'
    if 'LinkHtml' in data:
        link = data['LinkHtml']

        # Descargar el archivo HTML
        response = requests.get(link)

        if response.status_code == 200:
            # Guardar el archivo descargado en la carpeta estática
            temp_file_path = os.path.join(TEMP_FOLDER, 'pagina.html')
            with open(temp_file_path, 'wb') as file:
                file.write(response.content)

            # Redirigir al navegador al archivo guardado a través de la ruta definida
            return redirect(f'/static/temp_files/pagina.html')
        else:
            return jsonify({"error": "No se pudo descargar el archivo HTML"}), 500
    else:
        return jsonify({"error": "No se encontró el parámetro 'LinkHtml'"}), 400

# Ruta para servir archivos desde temp_files
@app.route('/static/temp_files/<filename>')
def serve_temp_file(filename):
    # Forzar el tipo de contenido a 'text/html' para que el navegador lo muestre
    return send_from_directory(TEMP_FOLDER, filename, mimetype='text/html')
