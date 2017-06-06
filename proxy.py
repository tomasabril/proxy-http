

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
    proibido = 'jogo'

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
        size = 10000
        data = sock_client.recv(size)
        if not data: return 'sem dados'
        
        print("\n---- header recebido ---------------------------\n")
        datastr = data.decode()
        print(datastr)
        header = datastr.split('\n')
        command, site, protocol = header[0].split(' ')
        host = header[1].split(' ')[1]
        command.strip()
        site.strip()
        protocol.strip()
        host.strip()
        print('command: {}'.format(command))
        print('site: {}'.format(site))
        print('protocol: {}'.format(protocol))
        print('host: {}'.format(host))
 
        if self.proibido in datastr:
            sock_client.send(b'HTTP/1.0 200 OK\n')
            sock_client.send(b'Content-Type: text/html\n')
            sock_client.send(b'\n') # header and body should be separated by additional newline
            sock_client.send('<html><body> <h1>Hello World</h1> Nao pode!! </body></html>'.encode())
        else:
            # Set the response to echo back the recieved data
            #sock_client.send(b'HTTP/1.0 200 OK\n')
            #sock_client.send(b'Content-Type: text/html\n')
            #sock_client.send(b'\n') # header and body should be separated by additional newline
            #sock_client.send('<html><body> <h1>Hello World</h1> Esse pode!! </body></html>'.encode())
            resposta = self.pega_site(command, site, host)
            sock_client.send(resposta)
        sock_client.close()

    def pega_site(self, command, site, host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((host, 80))
        print('conectando com {}:{}'.format(host, 80))
        sock.send('''{} {} HTTP/1.1\n
                Host: {}\n
                User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0\n
                Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n
                Accept-Language: en-US,en;q=0.5\n
                Accept-Encoding: gzip, deflate\n
                Connection: keep-alive\n'''.format(command, site, host).encode())
        return sock.recv(10000)


if __name__ == '__main__':
    server = ProxyServer('localhost', 8078)
    try:
        server.listen()
    except KeyboardInterrupt:
        print("\nCtrl C - Stopping server")
sys.exit(1)
