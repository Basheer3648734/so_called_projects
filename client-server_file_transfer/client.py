from socket import *
print('Hey this is client')
s=socket(AF_INET,SOCK_STREAM)
s.connect((gethostname(),1234))
while True:
    print(s.recv(1024).decode('utf-8'))
    break