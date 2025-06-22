import decrypt
import extractmsg
path=input("Enter path of the image: ")
encrypted_data=extractmsg.extract_message_from_image(path)
decrypted_data=decrypt.denc(encrypted_data)
print(f"Decrypted data: {decrypted_data}")