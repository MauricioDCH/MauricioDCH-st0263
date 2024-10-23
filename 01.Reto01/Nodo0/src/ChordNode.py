from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
from bootstrap import Bootstrap
import json
import os

# Definición de la clase del servidor gRPC
class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        self.nodes = []  # Lista para mantener la información de los nodos
        self.node_id = 0
        bootstrap = Bootstrap()
        self.node_ip = bootstrap.obtener_ip_global()
        self.node_port = 50051
        self.crear_archivo_json()

    def crear_archivo_json(self):
        url = f'{self.node_ip}:{self.node_port}'
        node_0 = {"NodeID": self.node_id, "URL": url, "Predecessor": self.node_id, "Successor": self.node_id}
        self.nodes.append(node_0)
        os.makedirs('../configs', exist_ok=True)
        with open('../configs/settings_Chord_Node.json', 'w') as f:
            json.dump(node_0, f, indent=4)
        print("Archivo JSON creado.")

    def HandleBootstrap(self, request, context):        
        print("Received bootstrap request:", request)
        if not request.node_ip or not request.node_port:
            print("Error: node_ip or node_port is empty")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("node_ip or node_port is empty")
            return peerCommunications_pb2.BootstrapResponse()
        
        # Incrementar el ID del nodo
        self.node_id += 1
        node_id_client = self.node_id
        node_ip = request.node_ip
        node_port = request.node_port
        url = f"{node_ip}:{node_port}"
        
        # Modificación del sucesor y predecesor del nodo 0.
        self.nodes[0]['Predecessor'] = node_id_client
        self.nodes[0]['Successor'] = self.nodes[0]['NodeID'] + 1
        
        # Buscar el nodo predecesor y sucesor
        predecessor = None
        successor = None
        if self.nodes:
            predecessor = self.nodes[-1]['NodeID']  # Ejemplo simplificado
            successor = self.nodes[0]['NodeID']
            self.nodes[-1]['Successor'] = node_id_client

        # Agregar el nuevo nodo a la lista
        new_node = {
            "NodeID": node_id_client,
            "URL": url,
            "Predecessor": predecessor,
            "Successor": successor
        }
        
        self.nodes.append(new_node)
        
        # Mostrar todos los nodos que se va ingresando
        for nodo in self.nodes:
            print(nodo)
        print()

        # Guardar en el archivo de configuración
        with open('../configs/settings_Chord_Node.json', 'w') as f:
            json.dump(self.nodes, f, indent=4)

        try:
            response = peerCommunications_pb2.BootstrapResponse(
                node_id_client      =   self.node_id,
                id_chord_node       =   self.nodes[0]['NodeID'],
                node_id_predeccesor =   predecessor if predecessor else 0,
                node_id_succesor    =   successor if successor else 0,
                node_status         =   True
            )
            return response
        except Exception as e:
            print("Error creating response:", e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error creating response")
            return peerCommunications_pb2.BootstrapResponse()

    def load_nodes(self):
        # Carga la configuración de nodos desde un archivo JSON
        try:
            with open('../configs/settings_Chord_Node.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return []
        except FileNotFoundError as e:
            print(f"Archivo JSON no encontrado: {e}")
            return []

    def GetData(self, request, context):
        print(f"GetData request received for node {request.node_id}")
        node_id = request.node_id

        # Cargar nodos desde el archivo JSON
        nodes = self.load_nodes()
        
        # Buscar el nodo en la configuración cargada
        node_data = next((node for node in nodes if node['NodeID'] == request.node_id), None)

        if node_data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Node not found")
            return peerCommunications_pb2.GetDataResponse()

        # Obtener el ID del sucesor
        node_id_succesor = node_data.get('Successor', 0)
        
        # Buscar los datos del sucesor
        successor_data = next((node for node in nodes if node['NodeID'] == node_id_succesor), None)
        
        if successor_data:
            node_ip_succesor = successor_data.get('URL', '')
            node_port_succesor = int(node_ip_succesor.split(':')[1])
        else:
            node_ip_succesor = ''
            node_port_succesor = 0
        
        response = peerCommunications_pb2.GetDataResponse(
            node_id_client=node_id,
            id_chord_node=nodes[0]['NodeID'],
            node_ip_chord_node=nodes[0]['URL'],
            node_id_predeccesor=node_data.get('Predecessor', 0),
            node_id_succesor=node_id_succesor,
            node_ip_succesor=node_ip_succesor,
            node_port_succesor=node_port_succesor,
            number_of_nodes_in_network=len(nodes)
        )
        
        return response



    def QueryFingerTable(self, request, context):
        print("QueryFingerTable request received")
        # Cargar nodos desde el archivo JSON
        nodes = self.load_nodes()

        # Crear listas para node_ids y node_urls
        node_ids = []
        node_urls = []

        for node_id_xd in request.node_ids:
            node_data = next((node for node in nodes if node['NodeID'] == node_id_xd), None)
            if node_data:
                node_ids.append(node_data['NodeID'])
                node_urls.append(node_data['URL'])
            else:
                print(f"Warning: node_id_xd {node_id_xd} not found in nodes list.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f"node_id_xd {node_id_xd} not found")
                # Enviar respuesta con listas vacías en caso de error
                return peerCommunications_pb2.FTResponse(node_ids=[], node_urls=[])

        # Construir la respuesta
        response = peerCommunications_pb2.FTResponse(
            node_ids=node_ids,
            node_urls=node_urls
        )
        return response


# Función principal para iniciar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
    peer2peer_servicer = Peer2PeerServicer()
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(peer2peer_servicer, server)
    #peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(Peer2PeerServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    #print(f"Servidor gRPC corriendo en {Peer2PeerServicer().node_ip}:50051")
    print(f"Servidor gRPC corriendo en {peer2peer_servicer.node_ip}:50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
