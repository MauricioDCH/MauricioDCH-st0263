import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import math

class QueryFingerTable:
    def __init__(self, m_number_of_nodes_in_network):
        self.m_number_of_nodes_in_network = m_number_of_nodes_in_network

    def generate_node_ids(self):
        # Calcula el tamaño de la tabla de finger
        finger_table_size = math.ceil(math.log2(self.m_number_of_nodes_in_network))
        print(f"Tamaño de la tabla de finger: {finger_table_size}")
        
        list_of_node_ids = []
        node_id_gmi = 0
        # Genera la lista de node_ids
        for ft_index in range(1, finger_table_size + 1):
            finger_id = math.ceil((node_id_gmi + 2**(ft_index - 1)) % self.m_number_of_nodes_in_network)
            list_of_node_ids.append(finger_id)
        
        print(f"Lista de node_ids generada: {list_of_node_ids}")
        return list_of_node_ids

    def request_finger_table(self):
        chord_address_node = 'localhost:50051'
        node_ids=self.generate_node_ids()
        # Configura la conexión con el servidor
        with grpc.insecure_channel(chord_address_node) as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)
            # Prepara la solicitud con una lista de node_ids
            #request_finger_table = peerCommunications_pb2.FTRequest(number_of_nodes_in_network=1, node_ids=[1, 2])
            
            
            request_finger_table = peerCommunications_pb2.FTRequest(
                number_of_nodes_in_network=self.m_number_of_nodes_in_network,
                node_ids=node_ids
            )
            
            print(f'Request: {request_finger_table}')
            # Envía la solicitud y recibe la respuesta
            try:
                response = stub.QueryFingerTable(request_finger_table)
                print("Respuesta del servidor:")
                dictionary = dict(zip(response.node_ids, response.node_urls))
                print(dictionary)
                return dictionary
            except grpc.RpcError as e:
                print(f"Error al comunicar con el servidor: {e.details()}")
