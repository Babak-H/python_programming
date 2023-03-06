import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# here we have connected to the address/port
client.connect(ADDR)

def send(msg):
    # format the message to utf-8 and then count its length
    message = msg.encode(FORMAT)
    msg_length = len(message)
    # create the length message (also encode that!) and then save it as a 64 bit size message
    send_length = str(msg_length).encode(FORMAT)
    # b' ' is an extra byte
    send_length += b' ' * (HEADER - len(send_length))
    # and send both messages in the order
    client.send(send_length)
    client.send(message)
    # message that we get from the server / we set an arbitrary large number, so server doesn't need to send us back a header too.
    print(client.recv(2048).decode(FORMAT))
    
send("Hello World!!")
send("Hi its Babak")
send(DISCONNECT_MESSAGE)
    
    
