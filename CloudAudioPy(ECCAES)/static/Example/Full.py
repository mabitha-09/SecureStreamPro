from cryptography.fernet import Fernet
import random
from stegano import lsb
from ecies.utils import generate_key
from ecies import encrypt, decrypt
import base64, os


def unhide():
    privhex = '6e562c0e3f31c7a918b13477b2fff54aea4b16c5813c26cb2cd08d268ea29d91'
    filepath = "./static/Encrypt/78976.png"
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/Encrypt/' + str(tail)
    newfilepath2 = './static/Decode/' + str(tail)

    data = 0
    with open(newfilepath1, "rb") as File:
        data = base64.b64decode(File.read())

    # print(data)
    decrypted_secp = decrypt(privhex, data)
    # print("\nDecrypted:", decrypted_secp)
    with open(newfilepath2, "wb") as DFile:
        DFile.write(base64.b64decode(decrypted_secp))

    clear_message = lsb.reveal(newfilepath2)
    print(clear_message)

    dfk = "gjRkwnCoxEqc6b0cPBoXtFffoPLNy2KKm4PBBK839cY="
    key = dfk.encode()
    print(key)
    fernet = Fernet(key)
    encMessage = clear_message.encode()
    decMessage = fernet.decrypt(encMessage).decode()
    print("decrypted string: ", decMessage)

    privhex = decMessage

    filepath = "./static/Encrypt/78976.png"
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/Encrypt/' + str(tail)
    newfilepath2 = './static/Decrypt/' + str(tail)

    data = 0
    with open(newfilepath1, "rb") as File:
        data = base64.b64decode(File.read())

    print(data)
    decrypted_secp = decrypt(privhex, data)
    print("\nDecrypted:", decrypted_secp)
    with open(newfilepath2, "wb") as DFile:
        DFile.write(base64.b64decode(decrypted_secp))

unhide()


