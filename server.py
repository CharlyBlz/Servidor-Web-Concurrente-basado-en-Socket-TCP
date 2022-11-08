import socket #Librería para manejo de sockets
import threading #Librería para manejo de hilos

IP = socket.gethostbyname(socket.gethostname()) #Retorna la dirección IP de la máquina local
PORT = 8080 #Se define el puerto
ADDR = (IP, PORT) #Tupla que maneja la dirección IP y el puerto
SIZE = 1024 #Variable que maneja el tamaño del búfer de datos
FORMAT = "utf-8" #Variable que define el formato de los datos
DISCONNECT_MSG = "!Desconectado" #Mensaje de desconexión

def handle_client(conn, addr): #Función para manejo del cliente
    print(f"[Nueva Conexión] {addr} Conectado.") #Imprime en consola 
    try:
        connected = True #Variable connected se inicializa en verdadero
        while connected: #Ciclo while que se ejecuta mientras la variable 'connected' sea verdadera
            msg = conn.recv(SIZE).decode(FORMAT) #Variable 'msg', mediante el objeto 'conn', guarda los datos decodificados los cuales fueron recibidos mediante el búfer de datos
            #Recibe datos del socket y los almacena en un búfer, recv aplica únicamente a sockets conectados
            if msg:
                with open('holamundo.html','r') as f:
                    page_data=f.read()
                    print(page_data)
                    f.close()
                    conn.send(b"HTTP/1.0 200 OK\r\n")
                    conn.send(b'Content-Type: text/html\n')
                    conn.send(b'\n')
                    conn.send(page_data.encode())
                    return
                
    except IOError:
        conn.send("404 not found")
        conn.close() #Se cierra la comunicación mediante el método 'close' del objeto 'conn' de la clase socket

def main(): #Función principal que actúa como punto de ejecución del programa
    print("[Iniciando] El servidor está iniciado...") #Imprime mensaje en consola
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crea 'server', un objeto socket que especifica mediante argumentos el tipo de dirección IP a usar así como el protocolo de red
    server.bind(ADDR) #El objeto socket utiliza el método 'bind' para asociar el socket con la  dirección IP y puerto especificadas mediante la tupla ADDR
    server.listen() #Permite que el servidor acepte conexiones
    print(f"[Escuchando] El servidor está escuchando a: {IP}:{PORT}") #Imrpime la dirección IP y el puerto al cual escucha el servidor

    while True: #Ciclo while infinito 
        conn, addr = server.accept() #Devuelve un objeto que represent la conexión (conn) y la tupla que contiene al direccipon (addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #Crea el objeto de la clase threading 
        #con los argumentos que apuntan a la función que tendrá el hilo y la tupla, en este caso: conn y addr.
        thread.start() #Inicia el hilo
        print(f"[Conexiones activas] {threading.activeCount() - 1}") #Imprime en consola
        print("[Conxiones activas]", threading.activeCount() - 1, thread.getName())#Imprime en consola

if __name__ == "__main__": #Función que verifica si corre el módulo directamente o se importa de otro lado
    main()

