from socket import *

mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))

# Recv and print server response
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Enciar comando HELO e imprimir respuesta del servidor
heloCommand = 'HELLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Iniciar TLS
tlsCommand = 'STARTTLS\r\n'
clientSocket.send(tlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
    print('220 reply not received from server.')

# Asegurar la conexion con TLS
clientSocket = ssl.wrap_socket(clientSocket)

# Enviar comando MAIL FROM e imprimir respuesta del servidor
mailFromCommand = 'MAIL FROM: test@example.com\r\n'
clientSocket.send(mailFromCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Enviar comando RCPT TO e imprimir respuesta del servidor
rcptToCommand = 'RCPT TO: recipient@example.com\r\n'
clientSocket.send(rcptToCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

# Enviar comando DATA e imprimir respuesta del servidor
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Enviar mensaje
messageData = 'Subject: Test email\r\n\r\nThis is a test message.'
clientSocket.send(messageData.encode())

# Mensaje termina con un solo periodo
period = '.\r\n'
clientSocket.send(period.encode())

# Enviar comando QUIT y obtener la respuestaa del servidor
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
clientSocket.close()
