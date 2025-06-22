from PIL import Image
def binary_to_text(binary_data):
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:
            continue  
        text += chr(int(byte, 2))
    return text
def extract_message_from_image(image_path):
    image = Image.open(image_path).convert("RGB")
    binary_data = ""
    end_marker = "1111111111111110"

    for pixel in image.getdata():
        for color in pixel: 
            lsb = bin(color)[-1]
            binary_data += lsb
            if binary_data.endswith(end_marker):
                message_bits = binary_data[:-16]
                return binary_to_text(message_bits)
    return "No hidden message found."

