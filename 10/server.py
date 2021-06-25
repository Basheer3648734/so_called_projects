from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind((gethostname(),1234))
s.listen(10)
with open('test.txt') as f:
    data=f.read()
while True:
    cli,add=s.accept()
    if add: 
        print(f'connection is established with {add}')
        cli.send(bytes(data,'utf-8'))
        break