"""
Realizado por:
Cesar A. Diaz - 1075235
Salma I. Mármol - 1085618

"""

import smtplib #para el correo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import py7zr #para comprimir los archivos
import hashlib #para realizar el hash
import getpass #para los passwords
a = ""

def comprimir(a):
    a = getpass.getpass("Indique el password del archivo: ")
    with py7zr.SevenZipFile('test.7z','w', password= a) as archive:
          archive.writeall('test.txt','base')

class HASH:
    def hashes(h):
        digest = h.hexdigest()
        return digest
     
x = 0
if x<1:
    print("Elige el algoritmo de comprobación a usar:")
    print("1. SHA-256")
    print("2. SHA-512")
    print("3. MD5")
    print("4. SHA-1")
    print("5. SHA3-224")
    
    print()
    nAlgoritm = int(input())

    algoritmo = ""

    if nAlgoritm != 6:
        if nAlgoritm == 1:
            algoritmo = "sha256"
        elif nAlgoritm == 2:
            algoritmo = "sha512"
        elif nAlgoritm == 3:
            algoritmo = "md5"
        elif nAlgoritm == 4:
            algoritmo = "sha1"
        elif nAlgoritm == 5:
            algoritmo = "sha3_224"
        
        a_file = open("test.txt", "rb")
        data = a_file.read()
        bdata = bytes(str(data),'utf-8')
        h = hashlib.new(algoritmo,bdata)
        
        hash1 = HASH.hashes(h)
        print("Hash de comprobación: ")
        print(hash1)
        print()
        


def main():
 #Parametros del correo
 Correo_gmail = input('Inserte el correo electronico: ')
 Pss_gmail = getpass.getpass("Indique la password: ")
 Dest_gmail = input("Indique a que correo va dirigido: ")
 asunto_gmail = input ("Indique su asunto: ")
 
 #parametros del script 
 remitente = Correo_gmail
 destinatario = Dest_gmail
 asunto = '[CSCipher] ' + str(asunto_gmail)
 cuerpo = 'Este es su hash de comprobación: ' + HASH.hashes(h) 
 ruta_adjunto = 'test.7z'
 nombre_adjunto ='test.7z'

 #creacion del objeto mensaje
 mensaje = MIMEMultipart()

 #atributos del mensaje
 mensaje['From'] = remitente
 mensaje['To'] = destinatario
 mensaje['Subject'] = asunto

 #Agrega el cuerpo del mensaje como objeto MIME de tipo texto
 mensaje.attach(MIMEText(cuerpo,'plain'))

 #Abrir el archivo que se va a adjuntar
 archivo_adjunto = open(ruta_adjunto,'rb')

 #se crea un objeto MIME base
 adjunto_MIME = MIMEBase('application','octet-stream')
 #se agrega adjunto
 adjunto_MIME.set_payload((archivo_adjunto).read())
 #se codifica el texto en BASE64
 encoders.encode_base64(adjunto_MIME)
 #cabecera del objeto
 adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
 # Y finalmente lo agregamos al mensaje
 mensaje.attach(adjunto_MIME)

 # Creamos la conexión con el servidor
 sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

 # Ciframos la conexión
 sesion_smtp.starttls()

 # Iniciamos sesión en el servidor
 sesion_smtp.login(Correo_gmail,Pss_gmail)

 # Convertimos el objeto mensaje a texto
 texto = mensaje.as_string()

 # Enviamos el mensaje
 sesion_smtp.sendmail(remitente, destinatario, texto)

 # Cerramos la conexión
 sesion_smtp.quit()

#orden de ejecución del programa
HASH.hashes(h)
comprimir(a)
main()



 
