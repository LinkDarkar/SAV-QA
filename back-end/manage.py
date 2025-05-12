import os
import json
from flask import Flask, request, jsonify, redirect, send_from_directory
import tempfile
import shutil
import requests

from GoogleDriveHandler import conectDrive

app = Flask(__name__) # Crear una instancia de la aplicación Flask

ROOT_DIR = os.path.dirname(__file__)
JSON_FILE_PATH = os.path.join(ROOT_DIR, 'Json', 'redirect.json')  # Ruta al archivo JSON
TEMP_FOLDER = os.path.join(ROOT_DIR, 'static', 'temp_files') # Ruta para almacenar archivos temporales
os.makedirs(TEMP_FOLDER, exist_ok=True) # Asegurarse de que la carpeta de archivos temporales exista

@app.route('/list/results')
def listResults():
    # Llamada para listar los archivos en Google Drive
    conectDrive.list_drive_files()
    return 'Archivos listados en la consola!'

# Ejecutar la aplicación
if __name__ == '__main__':
    listenPort = 5000
    try:
        app.run(host='0.0.0.0', port=listenPort, debug=True)
    except Exception as e:
        print("ERROR MAIN:", e)
