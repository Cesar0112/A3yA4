from socket import *
from base64 import *
from ssl import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
from email import encoders




endmsg = "\r\n.\r\n"

correo = destino = "cesarfernandezgarcia349@gmail.com"
clave = "lelp feet yrwg bean"


while True:
    print("Elija una opción\n")
    print("0-Salir")
    print("1-Mandar imagen")
    print("Cualquier letra para mandar solo texto")
    
    opcion = input(">")

    if(opcion == "1"):
        # Crea un mensaje multipart
        msg = MIMEMultipart()
        msg['From'] = 'tu_email@gmail.com'
        msg['To'] = 'destinatario@example.com'
        msg['Subject'] = 'Asunto del correo'

        # Añade el texto del mensaje
        message = "Hola, este es un mensaje con una imagen adjunta."
        msg.attach(MIMEText(message, 'plain'))

        # Añade la imagen al mensaje
        ruta_imagen = 'estudiantes.jpg'
        with open(ruta_imagen, 'rb') as imagen:
            img = MIMEImage(imagen.read())
            msg.attach(img)
    if(opcion == "0"):
        break
    
    if(opcion != "1"):    
        msg = "\r\nI love computer networks!"

    # Elige un servidor de correo (por ejemplo, el servidor de correo de Google) y llámalo mailserver
    mailserver = "smtp.gmail.com"
    port = 587

    # Crea un socket llamado clientSocket y establece una conexión TCP con mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Recibe el mensaje de saludo del servidor
    recv = clientSocket.recv(1024).decode()
    if(recv != ""):
        print("Saludo del servidor: "+recv)
    if recv[:3] != '220':
        print('No se recibió la respuesta 220 del servidor.')
    else:
        print("Todo fue correctamente con la conexión al servidor")
        
    # Envía el comando HELO y muestra la respuesta del servidor
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if(recv1 != ""):
        print("Respuesta al HELO Alice antes de la encriptacion: "+recv1)

    if recv1[:3] != '250':
        print('No se recibió la respuesta 250 del servidor.')
    else:
        print("Se ejecutó correctamente el comando HELO Alice")

    # Envía el comando STARTTLS y muestra la respuesta del servidor
    starttlsCommand = 'STARTTLS\r\n'
    clientSocket.send(starttlsCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    if(recv2 != ""):
        print("Respuesta al comando STARTTLS: "+recv2)
    if recv2[:3] != '220':
        print('No se recibió la respuesta 220 del servidor.')
    else:
        print("Se ejecutó correctamente el comando STARTTLS")
        
    # Encripta la conexión usando SSL/TLS

    clientSocket = wrap_socket(clientSocket)

    # Envía el comando HELO nuevamente después de la encriptación y muestra la respuesta del servidor
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    if(recv3 != ""):
        print("Respuesta al comando HELO Alice despues del encriptado: "+recv3)

    if recv3[:3] != '250':
        print('No se recibió la respuesta 250 del servidor.')
    else:
        print("Se ejecutó correctamente el comando HELO Alice")
        
    # Envía el comando AUTH LOGIN y muestra la respuesta del servidor
    authCommand = 'AUTH LOGIN\r\n'
    clientSocket.send(authCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    if(recv4 != ""):
        print("Respuesta al comando AUTH LOGIN: "+recv4)

    if recv4[:3] != '334':
        print('No se recibió la respuesta 334 del servidor.')
    else:
        print("Se ejecutó correctamente el comando AUTH LOGIN")
        
    # Envía el nombre de usuario y muestra la respuesta del servidor

    username = b64encode(correo.encode()) + b'\r\n'
    clientSocket.send(username)
    recv5 = clientSocket.recv(1024).decode()

    if(recv5 != ""):
        print("Respuesta al enviar el nombre de usuario: "+recv5)
    if recv5[:3] != '334':
        print('No se recibió la respuesta 334 del servidor.')
    else:
        print("Se envió correctamente el nombre de usuario")
        
    # Envía la contraseña y muestra la respuesta del servidor
    password = b64encode(clave.encode()) + b'\r\n'
    clientSocket.send(password)
    recv6 = clientSocket.recv(1024).decode()

    if(recv6 != ""):
        print("Respuesta al enviar la contraseña: "+recv6)
    if recv6[:3] != '235':
        print('No se recibió la respuesta 235 del servidor. Al enviar la contraseña')
    else:
        print("Las credenciales son correctas")
        
    # Envía el comando MAIL FROM y muestra la respuesta del servidor
    mailFromCommand = f'MAIL FROM: <{correo}>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv7 = clientSocket.recv(1024).decode()

    if(recv7 != ""):
        print("Respuesta al comando MAIL FROM: "+recv7)
    if recv7[:3] != '250':
        print('No se recibió la respuesta 250 del servidor.')
    else:
        print("Se ejecutó correctamente el comando MAIL FROM")

    # Envía el comando RCPT TO y muestra la respuesta del servidor
    rcptToCommand = f'RCPT TO: <{destino}>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv8 = clientSocket.recv(1024).decode()

    if(recv8 != ""):
        print("Respuesta al comando RCPT TO: "+recv8)
    if recv8[:3] != '250':
        print('No se recibió la respuesta 250 del servidor.')
    else:
        print("Se ejecutó correctamente el comando RCPT TO")
    # Envía el comando DATA y muestra la respuesta del servidor
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv9 = clientSocket.recv(1024).decode()

    if(recv9 != ""):
        print("Respuesta al comando DATA: "+recv9)
    if recv9[:3] != '354':
        print('No se recibió la respuesta 354 del servidor.')
    else:
        print("Se ejecutó correctamente el comando DATA")
    # Envía los datos del mensaje
    
    objetoEnviado = ""
    if(opcion == "1"):
        messageData = msg.as_string() + endmsg
        objetoEnviado = "IMAGEN"
    else:
        messageData = 'Subject: Prueba de correo electrónico\r\n' + msg + endmsg
        objetoEnviado = "TEXTO"
    clientSocket.send(messageData.encode())

    # Envía el comando QUIT y muestra la respuesta del servidor
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv10 = clientSocket.recv(1024).decode()
    if(recv10 != ""):
        print("Respuesta al comando QUIT: "+recv10)
    if recv10[:3] != '250':
        print('No se recibió la respuesta 250 del servidor.')
    else:
        print("Se ejecutó correctamente el comando QUIT")
        print(f"!!!!!!!!!!!!!! SE ENVIÓ {objetoEnviado} !!!!!!!!!!!!!!!")
    
    # Cierra el socket
    clientSocket.close()
    print("Socket cerrado")
