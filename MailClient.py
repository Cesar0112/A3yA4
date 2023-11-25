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

# Envía el nombre de usuario y muestra la respuesta del servidor

username = base64.b64encode("cesarfernandezgarcia349@gmail.com".encode()) + b'\r\n'
clientSocket.send(username)
recv5 = clientSocket.recv(1024).decode()

if(recv5 != ""):
    print("Respuesta al enviar el nombre de usuario: "+recv5)
if recv5[:3] != '334':
    print('No se recibió la respuesta 334 del servidor.')

# Envía la contraseña y muestra la respuesta del servidor
password = base64.b64encode("lelp feet yrwg bean".encode()) + b'\r\n'
clientSocket.send(password)
recv6 = clientSocket.recv(1024).decode()

if(recv6 != ""):
    print("Respuesta al enviar la contraseña: "+recv6)
if recv6[:3] != '235':
    print('No se recibió la respuesta 235 del servidor. Al enviar la contraseña')

# Envía el comando MAIL FROM y muestra la respuesta del servidor
mailFromCommand = 'MAIL FROM: <cesarfernandezgarcia349@gmail.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv7 = clientSocket.recv(1024).decode()

if(recv7 != ""):
    print("Respuesta al comando MAIL FROM: "+recv7)
if recv7[:3] != '250':
    print('No se recibió la respuesta 250 del servidor.')

# Envía el comando RCPT TO y muestra la respuesta del servidor
rcptToCommand = 'RCPT TO: <cesarfernandezgarcia349@gmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv8 = clientSocket.recv(1024).decode()

if(recv8 != ""):
    print("Respuesta al comando RCPT TO: "+recv8)
if recv8[:3] != '250':
    print('No se recibió la respuesta 250 del servidor.')

# Envía el comando DATA y muestra la respuesta del servidor
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv9 = clientSocket.recv(1024).decode()

if(recv9 != ""):
    print("Respuesta al comando DATA: "+recv9)
if recv9[:3] != '354':
    print('No se recibió la respuesta 354 del servidor.')

# Envía los datos del mensaje
messageData = 'Subject: Prueba de correo electrónico\r\n' + msg + endmsg
clientSocket.send(messageData.encode())

# Envía el comando QUIT y muestra la respuesta del servidor
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv10 = clientSocket.recv(1024).decode()
if(recv10 != ""):
    print("Respuesta al comando QUIT: "+recv10)
if recv10[:3] != '250':
    print('No se recibió la respuesta 221 del servidor.')

# Cierra el socket
clientSocket.close()
print("Socket cerrado")
