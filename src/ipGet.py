import socket
def ipGet():
    return socket.gethostbyname(socket.gethostname())
    
