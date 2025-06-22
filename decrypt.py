from cryptography.fernet import Fernet as fr
def denc(msg):
    with open("answer.key","rb") as f:
        key=f.read()
    fernet=fr(key)
    return fernet.decrypt(msg).decode()
print(denc('gAAAAABoWBDO9SaBzbR7EvLCpIJTGzyqsjeMliH_e9_C_vLLYpHU0VVLZjLDNhhbhbZhqg1mtfCZUp2gz-LNU2MB284QmJjEqg=='))
