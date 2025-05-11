from pydrive2 import *

"""
    Lo que tengo pensado es que cuando alguien entra, se cree uno de estos y
    se llene dependiendo de lo que esté en el archivo que le corresponda a la
    persona.

    Entonces, la persona se mete, se autentican las cosas y se obtiene la lista
    de los documentos. Luego de obtener la lista de los documentos. Se
    actualizan los documentos que estén en el backend.
"""
class DriveDocs ():
    driveFolder = None  # la carpeta que le pertenece a la persona que acaba de entrar?

    # No se que estoy haciendo
    def __init__(self, driveFolder):
        self.driveFolder = driveFolder

    def GetFileList():
        print("test")
        # requiere de un proceso de verificación de antes?
        # digo, para poder luego hacer:
        # fileList = drive.ListFile({'q': query}).GetList()
        # y lo que viene antes claro.

