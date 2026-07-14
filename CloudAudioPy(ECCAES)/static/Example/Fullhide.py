from cryptography.fernet import Fernet
import random
from stegano import lsb
from ecies.utils import generate_key
from ecies import encrypt, decrypt
import base64, os


message = "ecd3f44cf31afa79744d42ee8a47c5931022e003e10cf2ae7c45c0474afbcbf3"

key = Fernet.generate_key()

print("key : ",key)
Decryptkey = key.decode()
print("Decryptkey : ",Decryptkey)


fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage.decode())

secret = lsb.hide("./static/upload/78976.jpg", encMessage.decode())

pathname, extension = os.path.splitext("./static/upload/78976.jpg")
filename = pathname.split('/')

imageName = filename[-1]+".png"

secret.save("./static/Encode/"+imageName)



secp_k = generate_key()
privhex = secp_k.to_hex()
pubhex = secp_k.public_key.format(True).hex()


filepath = "./static/Encode/"+imageName
head, tail = os.path.split(filepath)

newfilepath1 = './static/Encrypt/' + str(tail)


data = 0
with open(filepath, "rb") as File:
    data = base64.b64encode(File.read())  # convert binary to string data to read file

print("Private_key:", privhex, "\nPublic_key:", pubhex, "Type: ", type(privhex))
#print("Binary of the file:", data)
encrypted_secp = encrypt(pubhex, data)
#print("Encrypted binary:", encrypted_secp)

with open(newfilepath1, "wb") as EFile:
    EFile.write(base64.b64encode(encrypted_secp))


