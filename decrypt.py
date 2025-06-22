from cryptography.fernet import Fernet as fr
def denc(msg):
    with open("answer.key","rb") as f:
        key=f.read()
    fernet=fr(key)
    return fernet.decrypt(msg).decode()
