import socket
import base64
# Define el mensaje a enviar
msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Elige un servidor de correo (por ejemplo, el servidor de correo de Google) y llámalo mailserver
mailserver = "smtp.gmail.com"
port = 587

# Crea un socket llamado clientSocket y establece una conexión TCP con mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, port))

# Recibe el mensaje de saludo del servidor
recv = clientSocket.recv(1024).decode()
if(recv != ""):
    print("Saludo del servidor: "+recv)
if recv[:3] != '220':
    print('No se recibió la respuesta 220 del servidor.')

# Envía el comando HELO y muestra la respuesta del servidor
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
if(recv1 != ""):
    print("Respuesta al HELO Alice antes de la encriptacion: "+recv1)

if recv1[:3] != '250':
    print('No se recibió la respuesta 250 del servidor.')

# Envía el comando STARTTLS y muestra la respuesta del servidor
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
if(recv2 != ""):
    print("Respuesta al comando STARTTLS: "+recv2)
if recv2[:3] != '220':
    print('No se recibió la respuesta 220 del servidor.')

# Encripta la conexión usando SSL/TLS
import ssl
clientSocket = ssl.wrap_socket(clientSocket)

# Envía el comando HELO nuevamente después de la encriptación y muestra la respuesta del servidor
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv3 = clientSocket.recv(1024).decode()

if(recv3 != ""):
    print("Respuesta al comando HELO Alice despues del encriptado: "+recv3)

if recv3[:3] != '250':
    print('No se recibió la respuesta 250 del servidor.')

# Envía el comando AUTH LOGIN y muestra la respuesta del servidor
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv4 = clientSocket.recv(1024).decode()

if(recv4 != ""):
    print("Respuesta al comando AUTH LOGIN: "+recv4)

if recv4[:3] != '334':
    print('No se recibió la respuesta 334 del servidor.')
