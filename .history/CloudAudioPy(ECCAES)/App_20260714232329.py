from flask import Flask, render_template, request, redirect, url_for, session, send_file
import mysql.connector
from ecies.utils import generate_key
from ecies import encrypt, decrypt
import base64, os

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ServerLogin')
def ServerLogin():

    return render_template('ServerLogin.html')


@app.route('/OwnerLogin')
def OwnerLogin():
    return render_template('OwnerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewOwner')
def NewOwner():
    return render_template('NewOwner.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/serverlogin", methods=['GET', 'POST'])
def serverlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='waiting'")
            data = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='Active'")
            data1 = cur.fetchall()
            return render_template('ServerHome.html', data=data, data1=data1)

        else:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)


@app.route("/ServerHome")
def ServerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route('/FileInfo')
def FileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()
    return render_template('FileInfo.html', data=data1)


@app.route("/UserApproved")
def UserApproved():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()
    return render_template('UserApproved.html', data=data, data1=data1)


@app.route("/Approved")
def Approved():
    id = request.args.get('lid')
    email = request.args.get('email')

    import random
    loginkey = random.randint(1111, 9999)
    message = "Owner Login Key :" + str(loginkey)

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("Update ownertb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()

    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/Approved1")
def Approved1():
    id = request.args.get('lid')
    email = request.args.get('email')

    import random
    loginkey = random.randint(1111, 9999)
    message = "User Login Key :" + str(loginkey)

    sendmail(email, message)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('UserApproved.html', data=data, data1=data1)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()
            alert = 'Record Saved!'
            return render_template('goback.html', data=alert)
        else:
            alert = 'Already Register This  UserName!'
            return render_template('goback.html', data=alert)


@app.route("/newowner", methods=['GET', 'POST'])
def newowner():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO ownertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()

            alert = 'Record Saved!'
            return render_template('goback.html', data=alert)
        else:
            alert = 'Already Register This  UserName!'
            return render_template('goback.html', data=alert)


@app.route("/ownerlogin", methods=['GET', 'POST'])
def ownerlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['oname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)

        else:

            Status = data[7]
            lkey = data[8]
            print(lkey)

            if Status == "waiting":

                alert = 'Waiting For Server Approved!'
                return render_template('goback.html', data=alert)

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='26clouddbaudiohidepy')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
                    data1 = cur.fetchall()
                    return render_template('OwnerHome.html', data=data1)
                else:
                    alert = 'Login Key Incorrect'
                    return render_template('goback.html', data=alert)


@app.route('/OwnerHome')
def OwnerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerHome.html', data=data1)


@app.route('/OwnerFileUpload')
def OwnerFileUpload():
    return render_template('OwnerFileUpload.html', oname=session['oname'])


'''from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes


def pad(data):
    # Add padding to make the data length a multiple of the block size (8 bytes for Blowfish)
    block_size = Blowfish.block_size
    padding_size = block_size - len(data) % block_size
    padding = bytes([padding_size]) * padding_size
    return data + padding


def unpad(data):
    # Remove padding from the decrypted data
    padding_size = data[-1]
    return data[:-padding_size]


def encrypt_file(input_file, output_file, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        file_out.write(cipher.iv)
        while True:
            chunk = file_in.read(1024)
            if len(chunk) == 0:
                break
            elif len(chunk) % 8 != 0:
                chunk = pad(chunk)
            encrypted_chunk = cipher.encrypt(chunk)
            file_out.write(encrypted_chunk)


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        iv = file_in.read(Blowfish.block_size)
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        while True:
            chunk = file_in.read(1024)
            if len(chunk) == 0:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            if len(chunk) < 1024:
                decrypted_chunk = unpad(decrypted_chunk)
            file_out.write(decrypted_chunk)'''


import pyAesCrypt
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits, N=10):
    return ''.join(random.choice(chars) for _ in range(N))


def aesencrypt(key, source, des):
    output = des
    pyAesCrypt.encryptFile(source, output, key)
    return output


def aesdecrypt(key, source, des):
    dfile = source.split(".")
    output = des

    pyAesCrypt.decryptFile(source, output, key)
    return output


@app.route("/owfileupload", methods=['GET', 'POST'])
def owfileupload():
    if request.method == 'POST':
        oname = session['oname']
        info = request.form['info']
        file = request.files['file']
        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename

        file.save("static/upload/" + savename)

        secp_k = generate_key()
        privhex = secp_k.to_hex()
        pubhex = secp_k.public_key.format(True).hex()

        print(pubhex)

        filepath = "./static/upload/" + savename
        head, tail = os.path.split(filepath)

        newfilepath1 = './static/Encrypt/' + str(tail)
        newfilepath2 = './static/Decrypt/' + str(tail)

        aesencrypt(pubhex, filepath, newfilepath1)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + savename + "','" + pubhex + "','" + pubhex + "')")
        conn.commit()
        conn.close()

        return render_template('OwnerFileUpload.html', pkey=pubhex, oname=oname)


@app.route('/OwnerFileInfo')
def OwnerFileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where OwnerName='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerFileInfo.html', data=data1)


@app.route("/ODownload")
def ODownload():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        prkey = data[5]
        fname = data[3]

    else:
        return 'Incorrect username / password !'

    privhex = prkey

    filepath = "./static/Encrypt/" + fname
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/Encrypt/' + str(tail)
    newfilepath2 = './static/Decrypt/' + str(tail)

    #key = bytes.fromhex(privhex)
    key = privhex
    aesdecrypt(key,filepath, newfilepath2 )

    return send_file(newfilepath2, as_attachment=True)


@app.route("/OwnerFileApproved")
def OwnerFileApproved():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and OwnerName='" + session['oname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and OwnerName='" + session['oname'] + "' ")
    data1 = cur.fetchall()
    return render_template('OwnerFileApproved.html', data=data, data1=data1)


@app.route("/OApproved")
def OApproved():
    rid = request.args.get('rid')
    fid = request.args.get('fid')

    session["fid"] = fid
    session["rid"] = rid

    return render_template('Hide.html')


import wave


def em_audio(af, string, output):
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
    waveaudio.close()
    print("Done...")


def ex_msg(af):
    print("Please wait...")
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
    msg = string.split("###")[0]
    print("Your Secret Message is: \033[1;91m" + msg + "\033[0m")
    waveaudio.close()


@app.route("/hide", methods=['GET', 'POST'])
def hide():
    if request.method == 'POST':
        from cryptography.fernet import Fernet
        import random
        

        Unhidekey = request.form['hkey']

        file = request.files['file']
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["rid"] + "'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            UserName = data[5]
        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  regtb where  UserName='" + UserName + "'")
        data1 = cursor.fetchone()
        if data1:
            session["email"] = data1[3]
        else:
            return 'Incorrect username / password !'

        # key encrypt
        message = prkey

        key = Fernet.generate_key()

        Decryptkey = key.decode()

        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())

        print("original string: ", message)
        print("encrypted string: ", encMessage)

        inname = "static/upload/" + savename

        outname = "./static/Encode/" + savename

        em_audio(inname, encMessage.decode(), outname)


        secp_k = generate_key()
        privhex = secp_k.to_hex()
        pubhex = secp_k.public_key.format(True).hex()

        # Read the file path of the selected file

        filepath = "./static/Encode/" + savename
        head, tail = os.path.split(filepath)

        newfilepath1 = './static/Encrypt/' + str(tail)
        # newfilepath2 = './static/Decrypt/' + str(tail)

        data = 0
        with open(filepath, "rb") as File:
            data = base64.b64encode(File.read())  # convert binary to string data to read file

        print("Private_key:", privhex, "\nPublic_key:", pubhex, "Type: ", type(privhex))
        # print("Binary of the file:", data)
        encrypted_secp = encrypt(pubhex, data)
        # print("Encrypted binary:", encrypted_secp)

        with open(newfilepath1, "wb") as EFile:
            EFile.write(base64.b64encode(encrypted_secp))

        imagedkey = privhex

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("update userfiletb set Status='Approved' ,ImageName='" + savename + "',Imagedkey='" + str(
            imagedkey) + "',Unhidekey='" + str(Unhidekey) + "', Decryptkey='" + str(Decryptkey) + "' where id='" +
                       session["rid"] + "'")
        conn.commit()
        conn.close()

        mailmsg = "Request Id" + session[
            "rid"] + "\nAudio decrypt key:" + imagedkey + "\nUnhidekey:" + Unhidekey + "\nDecryptkey: " + Decryptkey

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "projectmailm@gmail.com"
        toaddr = session["email"]

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Cloud Security"

        # string to store the body of the mail
        body = mailmsg

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = savename
        attachment = open("./static/Encrypt/" + savename, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "kkvz xxke jmeb pcyb")


        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()

        alert = 'key Hide and encrypt to Send to User'
        return render_template('goback.html', data=alert)


@app.route("/UDownload")
def UDownload():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and Username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and Username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


@app.route("/userdownload")
def userdownload():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "'")
    data = cursor.fetchone()
    if data:
        OwnerName = data[2]

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  ownertb where  UserName='" + OwnerName + "'")
    data = cursor.fetchone()
    if data:
        session['omail'] = data[3]

    return render_template('UnHide.html')


@app.route("/unhide", methods=['GET', 'POST'])
def unhide():
    if request.method == 'POST':
        from cryptography.fernet import Fernet
        import random
        

        idk = request.form['idk']
        uhk = request.form['uhk']
        dfk = request.form['dfk']

        file = request.files['file']

        file.save("static/Uupload/" + file.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Imagedkey='" + idk + "'")
        data = cursor.fetchone()
        if data:

            privhex = idk

            filepath = "./static/Uupload/" + file.filename
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Uupload/' + str(tail)
            newfilepath2 = './static/Decode/' + str(tail)

            data = 0
            with open(newfilepath1, "rb") as File:
                data = base64.b64decode(File.read())

            print(data)
            decrypted_secp = decrypt(privhex, data)
            print("\nDecrypted:", decrypted_secp)
            with open(newfilepath2, "wb") as DFile:
                DFile.write(base64.b64decode(decrypted_secp))

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
            cursor = conn.cursor()
            cursor.execute(
                "SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Unhidekey='" + uhk + "'")
            data = cursor.fetchone()
            if data:

                # clear_message = lsb.reveal(newfilepath2)

                mimage = newfilepath2

                print("Please wait...")
                waveaudio = wave.open(mimage, mode='rb')
                frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
                extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
                string = "".join(
                    chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
                msg = string.split("###")[0]
                print("Your Secret Message is: \033[1;91m" + msg + "\033[0m")
                waveaudio.close()
                # flash('Successfully Unhide Message!')
                clear_message = msg

                print(msg)

                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='26clouddbaudiohidepy')
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Decryptkey='" + dfk + "'")
                data = cursor.fetchone()
                if data:
                    fname = data[3]

                    key = dfk.encode()
                    print(key)
                    fernet = Fernet(key)
                    encMessage = clear_message.encode()
                    decMessage = fernet.decrypt(encMessage).decode()
                    print("decrypted string: ", decMessage)

                    privhex = decMessage

                    filepath = "./static/Encrypt/" + fname
                    head, tail = os.path.split(filepath)

                    newfilepath1 = './static/Encrypt/' + str(tail)
                    newfilepath2 = './static/Decrypt/' + str(tail)

                    key = (privhex)

                    aesdecrypt(key,newfilepath1, newfilepath2)

                    return send_file(newfilepath2, as_attachment=True)




                else:

                    sendmail(session['omail'], "Unauthorized Access Your File")

                    alert = 'Decrypt file key Incorrect!'
                    return render_template('goback.html', data=alert)



            else:
                sendmail(session['omail'], "Unauthorized Access Your File")
                alert = 'Audio unhide key Incorrect!'
                return render_template('goback.html', data=alert)




        else:
            sendmail(session['omail'], "Unauthorized Access Your File")
            alert = 'Audio decrypt key Incorrect!'
            return render_template('goback.html', data=alert)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)

        else:

            Status = data[7]
            lkey = data[8]

            if Status == "waiting":

                alert = 'Waiting For Server Approved!'
                return render_template('goback.html', data=alert)

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='26clouddbaudiohidepy')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
                    data1 = cur.fetchall()
                    return render_template('UserHome.html', data=data1)
                else:
                    alert = 'Login Key Incorrect'
                    return render_template('goback.html', data=alert)


@app.route('/UserHome')
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserHome where OwnerName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('UserHome.html', data=data1)


@app.route('/USearch')
def USearch():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()
    return render_template('USearch.html', data=data1)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        sear = request.form['sear']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM filetb where ownername like'%" + sear + "%' or FileInfo like'%" + sear + "%' or FileName like '%" + sear + "%' ")
        data1 = cur.fetchall()
        return render_template('USearch.html', data=data1)


@app.route("/SendKeyRequest")
def SendKeyRequest():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[1]
        fname = data[3]
        prkey = data[5]

    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO userfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'uname'] + "','waiting','','','','')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='26clouddbaudiohidepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "kkvz xxke jmeb pcyb")


    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    # app.run(debug=True, use_reloader=True)
