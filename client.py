import socket

IP = socket.gethostbyname(socket.gethostname()) #Retorna la dirección IP de la máquina local
PORT = 8080 #Se define el puerto
ADDR = (IP, PORT) #Tupla que maneja la dirección IP y el puerto
SIZE = 1024 #Variable que maneja el tamaño del búfer de datos
FORMAT = "utf-8" #Variable que define el formato de los datos
DISCONNECT_MSG = "!Desconectado" #Mensaje de desconexión

def main(): #Fucnión principal
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crea 'client', un objeto socket que especifica mediante argumentos el tipo de dirección IP a usar así como el protocolo de red
    client.connect(ADDR) #El objeto socket "client" establece una conexión con el servidor e inixia el handshake de tres vías
    print(f"[Conectado] Cliente conectado a: {IP}:{PORT}") #Imprime en consola la tupla de dirección y puerto del servidor al cual se conectó el cliente 

    connected = True #Se inicializa en verdadero varible "connected"
    while connected: #Ciclo mientras la variable sea verdadera
        msg = input("Mensaje a mandar: ") #El mensaje es igual a lo que el usuario ingrese mediante consola

        client.send(msg.encode(FORMAT)) #Se envía el mensaje condificado en formato utf-8


if __name__ == "__main__":#Función que verifica si corre el módulo directamente o se importa de otro lado
    main()