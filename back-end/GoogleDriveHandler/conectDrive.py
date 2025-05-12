import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Ruta absoluta al archivo de credenciales, usando os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual de conectDrive.py
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, '..', 'service_account', 'sav-qa-cb1d8d7fc5fa.json')

# El alcance de acceso a Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Autenticación con la cuenta de servicio
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Función para obtener el servicio de Google Drive
def get_drive_service():
    try:
        # Construir el servicio de Google Drive
        service = build('drive', 'v3', credentials=credentials)
        return service
    except HttpError as error:
        print(f'Error al acceder a Google Drive: {error}')
        return None

def list_drive_files():
    service = get_drive_service()
    folder_id = '1UYrEJtrQ4TCB-byLBAsE6riIAE-Nt4eT'
    if service:
        try:
            # Llamada a la API para listar archivos dentro de una carpeta específica
            results = service.files().list(
                q=f"'{folder_id}' in parents",  # Filtra archivos dentro de la carpeta especificada
                pageSize=10, 
                fields="nextPageToken, files(id, name)"
            ).execute()

            items = results.get('files', [])
            
            if not items:
                print('No se encontraron archivos en la carpeta.')
            else:
                print('Archivos en la carpeta de Google Drive:')
                for item in items:
                    print(f'{item["name"]} ({item["id"]})')

        except HttpError as error:
            print(f'Ocurrió un error al listar los archivos: {error}')