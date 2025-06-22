import addmsg
import encrypt
import format
import meme
import os
userinput=input("Enter your message: ")
encrypted_data=encrypt.enc(userinput)
path_image=meme.memegetter()
format.form(path_image)
new_path_image=path_image.split('.')[0]+'.png'
addmsg.stegan(new_path_image,encrypted_data)
os.remove(path_image)
print("Done")
