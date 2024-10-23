import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc

class Client:

    def __init__(self):
        pass



    def queryFileList(self):
        # Conectar al servidor gRPC
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)

            # Crear una solicitud con todos los campos necesarios
            request = peerCommunications_pb2.FileListRequest(
                node_id_required=0,
                node_ip_required="some_ip",
                node_port_required=50051,
                next_node_id=2,
                next_node_ip="next_node_ip",
                next_node_port=50051,
            )

            # Llamar al método QueryFileList con la solicitud
            response = stub.QueryFileList(request)

            # Imprimir la lista de archivos recibida
            print("Lista de archivos recibida:", response.file_list)
            print("Ubicación de los archivos:", response.file_locations)

    def uploadFile(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)

            # Solicitar al usuario el nombre y la ubicación del archivo a subir
            file_name = 'example.txt'
            file_location = '../sources'

            # Crear una solicitud
            request = peerCommunications_pb2.UploadFileRequest(
                file_name=file_name,
                file_location=file_location
            )

            # Llamar al método UploadFile
            response = stub.UploadFile(request)
            
            # Imprimir la respuesta del servidor
            print("Respuesta del servidor:", response.status)

    def downloadFile(self):
        # Conectar al servidor gRPC
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)

            # Crear una solicitud con todos los campos necesarios
            request = peerCommunications_pb2.DownloadFileRequest(
                node_id_required=0,
                node_ip_required="some_ip",
                node_port_required=50052,
                file_name='source_n_1_peer1.txt',
                file_location='../sources'
            )

            # Llamar al método DownloadFile con la solicitud
            response = stub.DownloadFile(request)

            # Imprimir la respuesta recibida
            print("Respuesta del servidor:", response.status)

    def Ping(self, request, context):
        pass

if __name__ == "__main__":
    quetyFileListv = Client()
    quetyFileListv.queryFileList()
    print("\n")
    quetyFileListv.uploadFile()
    print("\n")
    quetyFileListv.downloadFile()