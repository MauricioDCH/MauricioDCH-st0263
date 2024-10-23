import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import requests

class Bootstrap:
    def __init__(self):
        # IP global del nodo
        self.node_ip = self.obtener_ip_global()
    
    def obtener_ip_global(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Error al obtener la IP global: {e}")
            return "IP no disponible"
    
    def handle_bootstrap(self):
        port = 50051
        chord_address_node = 'localhost:50051'
        with grpc.insecure_channel(chord_address_node) as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)
            
            bootstrap_request = peerCommunications_pb2.BootstrapRequest(
                node_ip=self.node_ip,
                node_port=port
            )
            try:
                response = stub.HandleBootstrap(bootstrap_request)
                
                # Verificar la respuesta
                if response:
                    print(f"ID del nodo asignado: {response.node_id_client}")
                    print(f"ID del nodo Chord: {response.id_chord_node}")
                    print(f"ID del nodo predecesor: {response.node_id_predeccesor}")
                    print(f"ID del nodo sucesor: {response.node_id_succesor}")
                    print(f"Estado del nodo: {'Activo' if response.node_status else 'Inactivo'}")
                else:
                    print("No se recibió respuesta del servidor.")
                
                return response
            except grpc.RpcError as e:
                print(f'Error al comunicar con el nodo Chord: {e.details()}')
                return None
