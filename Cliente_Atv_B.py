# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = '10.13.7.127' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = input('Digite o comando.')

clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
arquivoMessage = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, arquivoMessage.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente