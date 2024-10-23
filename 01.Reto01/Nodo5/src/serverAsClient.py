import time
from bootstrap import Bootstrap
from getData import GetData
from FingerTableGenerator import QueryFingerTable

import json

def create_set_json(boots_response, get_data_response, ft_response, filename='../configs/settings.json'):
    """
    Crea un archivo JSON con las respuestas BOOTS, GET y FT.

    :param boots_response: Diccionario con la respuesta BOOTS.
    :param get_data_response: Diccionario con la respuesta GET.
    :param ft_response: Diccionario con la respuesta FT.
    :param filename: Nombre del archivo JSON a crear.
    """
    # Estructura del contenido JSON
    data = {
        "BOOTSTAP": boots_response,
        "GETDATA": get_data_response,
        "FINGERTABLE": ft_response
    }

    # Escribir los datos en el archivo JSON
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Archivo JSON "{filename}" creado exitosamente.')

def serverAsClient():
    print('INICIANDO CLIENTE...')
    
    # BOOTSTRAP
    print("BOOTSTRAP")
    bootstrap = Bootstrap()
    bootResponse = bootstrap.handle_bootstrap()
    print(f"ID del nodo asignado: {bootResponse.node_id_client}")
    
    time.sleep(1)
    
    # GET DATA
    print("\nGET DATA")
    getData = GetData()
    getDataResponse = getData.get_data(bootResponse.node_id_client)
    print(getDataResponse)
    
    time.sleep(1)
    
    # FINGER TABLE
    print("\nFINGER TABLE")
    finger_table = QueryFingerTable(getDataResponse.number_of_nodes_in_network)
    #finger_table = QueryFingerTable(2)
    ftResonse = finger_table.request_finger_table()
    
    print('--------------------------------------------------------------')
    print(f'BOOTSTRAP: \n{bootResponse}')
    print(f'GET: \n{getDataResponse}')
    print(f'FT: \n{ftResonse}')
    
    boots_response = {
        "node_id_client": bootResponse.node_id_client,
        "node_id_predecessor": bootResponse.node_id_predeccesor,
        "node_status": bootResponse.node_status
    }
    
    get_data_response = {
        "node_id_client": getDataResponse.node_id_client,
        "node_ip_chord_node": getDataResponse.node_ip_chord_node,
        "node_id_predecessor": getDataResponse.node_id_predeccesor,
        "node_ip_successor": getDataResponse.node_ip_succesor,
        "node_port_successor": getDataResponse.node_port_succesor,
        "number_of_nodes_in_network": getDataResponse.number_of_nodes_in_network
    }
    ft_response = ftResonse
    create_set_json(boots_response, get_data_response, ft_response)

if __name__ == '__main__':
    serverAsClient()
