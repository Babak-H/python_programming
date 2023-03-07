import socket
import threading
from queue import Queue

target = socket.gethostbyname(socket.gethostname())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portScan(port):
    try:
        socket.connect((target, port))
        return True
    except:
        return False
    
    
# without use of thread and queue
'''
for port in range(1, 1024):
    result = portScan(port)
    if result:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
'''        
queue = Queue()
open_ports = []
thread_list = []

# we create a queue and then put all the open ports inside that queue. this way when we scan one port in multi-threaded way, it won't be scanned in other threads
def fill_queue(port_list):
    for port in port_list:
        # first in first out
        queue.put(port)
        
# here we get a port from queue, remove it from queue, and then scan it.
def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print(f"Port {port} is open")
            open_ports.append(port)
            
port_list = range(1, 1024)
fill_queue(port_list)

# create 100 threads and put worker function in each of them, here the thread is NOT running
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# start all threads   
for thread in thread_list:
    thread.start()
    
# the join method blocks the script until all threads are finished running
for thread in thread_list:
    thread.join()
    
print(f"Open ports are {open_ports}")