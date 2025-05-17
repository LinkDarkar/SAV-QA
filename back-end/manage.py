import os
import json
from flask import Flask, request, jsonify, redirect, send_from_directory
import tempfile
import shutil
import requests

from App import app
import App.routes
from GoogleDriveHandler import conectDrive

ROOT_DIR = os.path.dirname(__file__)
JSON_FILE_PATH = os.path.join(ROOT_DIR, 'Json', 'redirect.json')  # Ruta al archivo JSON
JSON_USERTEST_PATH = os.path.join(ROOT_DIR, 'Json', 'loginTests.json')
JSON_USERS_PATH = os.path.join(ROOT_DIR, 'Json', 'users.json')
JSON_COMPANIES_PATH = os.path.join(ROOT_DIR, 'Json', 'companies.json')
TEMP_FOLDER = os.path.join(ROOT_DIR, 'static', 'temp_files')  # Ruta para almacenar archivos temporales
os.makedirs(TEMP_FOLDER, exist_ok=True)  # Asegurarse de que la carpeta de archivos temporales exista


# Ejecutar la aplicación
if __name__ == '__main__':
    listenPort = 5000
    try:
        app.run(host='0.0.0.0', port=listenPort, debug=True)
    except Exception as e:
        print("ERROR MAIN:", e)
