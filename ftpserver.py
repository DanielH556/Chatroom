import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import ftplib as ftp

FTP_HOST = '192.168.15.141'
FTP_PORT = 21

ftp.login=('saet')
ftp.password=('aps')

def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('saet', 'aps', '.', perm='elradfmwMT')
    print('[+] Usuário adicionado')

    authorizer.add_anonymous(os.getcwd(), perm='elradfmwMT')
    print('[+] Usuário anônimo adicionado')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "chupa cu de goianinha"
    print('[+] Banner personalizado definido')

    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)

    # server.max_cons = 256
    # server.max_cons_per_ip = 5
    print('[+] Servidor FTP iniciado')

    server.serve_forever()

if __name__ == '__main__':
    main()