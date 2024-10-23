import subprocess
import threading

def run_server_as_server():
    # Ejecutar serverAsServer.py como un proceso separado
    subprocess.run(["python3", "serverAsServer.py"])

def main():
    # Ejecutar serverAsClient.py primero
    subprocess.run(["python3", "serverAsClient.py"])

    # Luego, ejecutar serverAsServer.py en un hilo separado
    server_thread = threading.Thread(target=run_server_as_server)
    server_thread.start()

if __name__ == "__main__":
    main()
