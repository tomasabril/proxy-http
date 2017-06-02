

#Tomás Abril

# ver http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
# e   https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
# https://docs.python.org/3/library/threading.html?highlight=threading#module-threading

import socket
import threading
import sys

print("oi")

class ProxyServer(object):
    """docstring for ."""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print('servidor Proxy iniciado em {}:{}'.format(self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            sock_client, addr_client = self.sock.accept()
            sock_client.settimeout(60)
            threading.Thread(target=self.client, args=(sock_client, addr_client)).start()

    def client(self, sock_client, addr):
        size = 1024
        while True:
            data = sock_client.recv(size)
            if data:
                # Set the response to echo back the recieved data
                response = data
                sock_client.send(response)
            else:
                sock_client.close()
                break


if __name__ == '__main__':
    server = ProxyServer('localhost', 8078)
    try:
        server.listen()
    except KeyboardInterrupt:
        print("\nCtrl C - Stopping server")
sys.exit(1)
