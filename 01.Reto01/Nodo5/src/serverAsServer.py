from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import json
from bootstrap import Bootstrap
from getData import GetData
from FingerTableGenerator import QueryFingerTable
import time
import os
class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        self.shared_files_dir = '../sources'
        self.shared_files = os.listdir(self.shared_files_dir)
        bootstrap = Bootstrap()
        self.ip_global = bootstrap.obtener_ip_global()  # Obtener IP global al inicializar la clase
        self.chord_address = 'localhost:50052'
        self.node_id = None  # Inicializa en None, se asignará después con HandleBootstrap

    def QueryFileList(self, request, context):        
        # Obtener la lista de archivos del nodo actual desde la carpeta 'sources'
        directory = "../sources"
        file_list = []

        if os.path.exists(directory):
            file_list = os.listdir(directory)

        # Crear un mensaje de respuesta con la lista de archivos
        response = peerCommunications_pb2.FileListResponse(
            file_list=file_list,
            file_locations=directory
            #file_locations=file_locations
        )

        # Retornar la respuesta al cliente
        return response

    def UploadFile(self, request, context):
        file_name = request.file_name
        file_location = request.file_location

        # Crear la ruta completa para el archivo
        file_path = os.path.join(file_location, file_name)

        try:
            # Aquí debes agregar la lógica para guardar el archivo en file_path
            # Este ejemplo simplemente indica que el archivo se ha subido
            with open(file_path, 'wb') as file:
                file.write(b"")  # Este es un ejemplo simplificado; aquí deberías escribir el contenido del archivo

            status = "Archivo subido exitosamente"
        except Exception as e:
            status = f"Error al subir el archivo: {str(e)}"

        response = peerCommunications_pb2.UploadFileResponse(status=status)
        return response


    def DownloadFile(self, request, context):
        file_name = request.file_name
        file_location = request.file_location

        # Construir la ruta completa del archivo
        file_path = os.path.join(file_location, file_name)

        if os.path.isfile(file_path):
            # En este ejemplo, no realmente leemos el archivo, solo enviamos un mensaje de éxito
            resultado = "Archivo descargado exitosamente"
        else:
            resultado = "Archivo no encontrado"

        response = peerCommunications_pb2.DownloadFileResponse(status=resultado)
        return response




def serve():
    print('INICIANDO SERVIDOR...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_servicer = Peer2PeerServicer()
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(server_servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(f'Servidor como Servidor iniciado en el puerto 50052 \n')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()