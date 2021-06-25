from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind((gethostname(),1234))
s.listen(10)
add=tuple()
while True:
    if add:
        try:
            k=input('enter msg')
            cli.send(bytes(k,'utf-8'))
            print(cli.recv(1024).decode('utf-8')+'- from client')
        except KeyboardInterrupt:
            print()
            print('exiting ------')
            break
    else:
        try:
            cli,add=s.accept()
            print(f'connection is established with {add}')
        except ConnectionError as e:
            print(e)