import socket
import threading
from queue import Queue

# target ip
target = "127.0.0.1"

#empty queue
queue = Queue()

open_ports = []


# connecting to the target server and finding open port
def port_scan(port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((target,port))
        return True
    except:
        return False



def append_queue(port_list):
    for port in port_list:
        queue.put(port)


# defining a function for getting single port from queue and appeding all the open port in open_port list
def port_scanner():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print(f"{port} is open!")
            open_ports.append(port)
        else:
            print(f"{port} is closed!")


#passing port from 1 to 1024 for cheacking
port_list = range(1,1024)

#sending one by one to the queue
append_queue(port_list)



# creating a list and function for threading with range 500 it send thread to target ip with 500 at one time
thread_list = []

for t in range(500):
    thread = threading.Thread(target= port_scanner())
    thread_list.append(thread)


# starting the thread
for thread in thread_list:
    thread.start()

#waiting the thread to complete
for thread in thread_list:
    thread.join()

#and last prinitng all the open prot from  open_port list
print("Open port are : ",open_ports)
