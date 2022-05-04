# importacao das bibliotecas
from socket import * # sockets
import time #time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    
    if(message != 'data'):
        serverSocket.sendto('Comando inválido', clientAddress)
    else:
        date = str(time.ctime())
        serverSocket.sendto(date.encode('utf-8'), clientAddress) 
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor