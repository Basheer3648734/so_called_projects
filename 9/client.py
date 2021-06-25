from socket import *
print('Hey this is client')
s=socket(AF_INET,SOCK_STREAM)
s.connect((gethostname(),1234))
while True:
    try:
        k=input('enter msg')
        s.send(bytes(k,'utf-8'))
        print(s.recv(1024).decode('utf-8')+'- from server')
    except KeyboardInterrupt:
        print()
        print('exiting -----')
        break