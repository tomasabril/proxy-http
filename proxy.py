

#Tomás Abril

# ver http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
# e   https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
# e  https://docs.python.org/3/library/threading.html?highlight=threading#module-threading

import socket
import threading
import sys
import time

print("oi")

class ProxyServer(object):
    """docstring for ."""

    proibido = 'jogo'
    size = 10000

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print('servidor Proxy iniciado em {}:{}'.format(self.host, self.port))

    def listen(self):
        self.sock.listen(300)
        while True:
            sock_client, addr_client = self.sock.accept()
            # sock_client.settimeout(60)
            threading.Thread(target=self.client, args=(sock_client, addr_client)).start()
            #time.sleep(.1)

    def client(self, sock_client, addr):
        data = sock_client.recv(self.size)
        #time.sleep(.1)
        
        if not data: return 'sem dados'

        print("\n---- header recebido ---------------------------")
        datastr = data.decode()

        header = datastr.split('\r\n')
        command, site, protocol = header[0].split(' ')
        host = header[1].split(' ')[1]

        if command == 'GET':
            print(datastr)
            print('command:  -{}-'.format(command))
            print('site:     -{}-'.format(site))
            print('protocol: -{}-'.format(protocol))
            print('host:     -{}-'.format(host))

        if self.proibido in site:
            sock_client.send(b'HTTP/1.0 200 OK\r\n')
            sock_client.send(b'Content-Type: text/html\r\n')
            sock_client.send(b'\r\n') # header and body should be separated by additional newline
            sock_client.send('<html><body> <h1>Acesso nao autorizado!</h1> Nao pode!! </body></html>'.encode())
        else:
            print('\nconectando com {}:{}'.format(host, 80))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # sock.settimeout(30)
            if command == 'GET':
                sock.connect((host, 80))
            elif command == 'CONNECT':
                conhost, conport = datastr.split('Host: ')[1].split(':')
                print('HOST: {}'.format(conhost))
                print('PORT: {}'.format(conport))
                sock.connect((conhost, int(conport)))
            else:
                print('================= erro ================ \ncomando não reconhecido')
            print('enviando dados...')
            sock.send(data)
            print('esperando resposta...')

            print('mandando resposta para browser...')
            while True:
                resposta = sock.recv(self.size)
                print(len(resposta))
                if not resposta: break
                sock_client.send(resposta)
            
            print('fechando conexão com servidor...')
            sock.close()
        print('fechando conexão com browser...')
        sock_client.close()


if __name__ == '__main__':
    server = ProxyServer('localhost', 8078)
    try:
        server.listen()
    except KeyboardInterrupt:
        print("\nCtrl C - Stopping server")
sys.exit(1)
