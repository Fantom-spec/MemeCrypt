from cryptography.fernet import Fernet as fr
def enc(msg):
    with open("answer.key","rb") as f:
        key=f.read()
    fernet=fr(key)
    return fernet.encrypt(msg.encode())
print(enc("Hello"))