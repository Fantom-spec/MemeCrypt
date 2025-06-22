from PIL import Image

def to_binary(data: str) -> str:
    return ''.join(format(ord(char), '08b') for char in data) + '1111111111111110'

def stegan(path, msg):
    msg = msg.decode()
    binary_data = to_binary(msg)
    img = Image.open(path)
    if img.mode != 'RGB':
        img = img.convert('RGB')    
    data = iter(img.getdata())
    new_pixels = []
    for i in range(0, len(binary_data), 3):
        pixel = list(next(data))
        for j in range(3):
            if i + j < len(binary_data):
                pixel[j] = pixel[j] & ~1 | int(binary_data[i + j])
        new_pixels.append(tuple(pixel))
    new_pixels += list(data)
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(path, format="PNG")
