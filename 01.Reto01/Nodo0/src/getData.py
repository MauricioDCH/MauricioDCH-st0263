import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import requests

class GetData:
    def __init__(self):
        # IP global del nodo
        self.node_ip = self.obtener_ip_global()
        # Node ID
    
    def obtener_ip_global(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Error al obtener la IP global: {e}")
            return "IP no disponible"
    
    def get_data(self, node_id):
        port = 50051
        chord_address_node = 'localhost:50051'
        with grpc.insecure_channel(chord_address_node) as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)
            
            get_data_request = peerCommunications_pb2.GetDataRequest(
                node_id=node_id,
                node_ip=self.node_ip,
                node_port=port
            )
            try:
                response = stub.GetData(get_data_request)
                
                # Verificar la respuesta
                if response:
                    print(f"ID del nodo cliente: {response.node_id_client}")
                    print(f"ID del nodo Chord: {response.id_chord_node}")
                    print(f"IP del nodo Chord: {response.node_ip_chord_node}")
                    print(f"ID del nodo predecesor: {response.node_id_predeccesor}")
                    print(f"ID del nodo sucesor: {response.node_id_succesor}")
                    print(f'IP del nodo sucesor: {response.node_ip_succesor}')
                    print(f'Puerto del nodo sucesor: {response.node_port_succesor}')
                    print(f"Número de nodos en la red: {response.number_of_nodes_in_network}")
                    return response
                else:
                    print("No se recibió respuesta del servidor.")
            
            except grpc.RpcError as e:
                print(f'Error al comunicar con el nodo Chord: {e.details()}')
                return None
