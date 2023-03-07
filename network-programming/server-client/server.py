import socket
import threading

# choose the port and server IP address
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # SERVER = "192.168.56.1"
print(SERVER)
# the size of the header message
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

# create the socket based on IPV4 addresses (family, type)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to the port and server
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        # here we will wait on this line of code, until we receive a message from our client
        # the first message after connection is telling us how long the next message is
        # this message is always 64 bytes in length (as we defined it)
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # make sure the message is not null
        if msg_length:
            msg_length = int(msg_length)
            # here also the thread is blocked until we receive the second message
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] {msg}")
            # here we want to send a message back to the client
            conn.send("we got your message!".encode(FORMAT))
        
    conn.close()


# listen for connection requests and handle them
def start():
    server.listen()
    while True:
        # save the ip address and port of the incoming connection
        conn, addr = server.accept()
        # handle each new connection request in a new thread via the handle_client function
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        

print("[STARTING] server is starting...")
start()
