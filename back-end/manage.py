import os
import json
from flask import Flask, request, jsonify, redirect, send_from_directory
import tempfile
import shutil
import requests

ROOT_DIR = os.path.dirname(__file__)
JSON_FILE_PATH = os.path.join(ROOT_DIR, 'Json', 'redirect.json')  # Ruta al archivo JSON

# Ruta de la carpeta donde se almacenarán los archivos temporales
TEMP_FOLDER = os.path.join(ROOT_DIR, 'static', 'temp_files')

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Asegurarse de que la carpeta de archivos temporales exista
os.makedirs(TEMP_FOLDER, exist_ok=True)

# Ruta para servir archivos desde temp_files
@app.route('/static/temp_files/<filename>')
def serve_temp_file(filename):
    # Forzar el tipo de contenido a 'text/html' para que el navegador lo muestre
    return send_from_directory(TEMP_FOLDER, filename, mimetype='text/html')

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

"""
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

            # Redirigir al navegador a la URL del archivo guardado
            # return redirect(f'/static/temp_files/pagina.html')
            
            return redirect(f'/static/temp_files/pagina.html')


        else:
            return jsonify({"error": "No se pudo descargar el archivo"}), 500

    else:
        return jsonify({"error": "No se encontró el parámetro"}), 400

"""
# Definir una ruta para manejar solicitudes POST y recibir un JSON
@app.route('/redirect/json', methods=['POST'])
def redirectWithJson():
    # Obtener el JSON enviado en la solicitud
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)  # Cargar el contenido del archivo JSON

    # Verificar si el JSON contiene un parámetro 'parametro'
    if 'Link' in data:
        link = data['Link']
        return redirect(link)
    else:
        return jsonify({"error": "No se encontró el parámetro"}), 400

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

# Ejecutar la aplicación
if __name__ == '__main__':
    listenPort = 5000
    try:
        app.run(host='0.0.0.0', port=listenPort, debug=True)
    except Exception as e:
        print("ERROR MAIN:", e)
