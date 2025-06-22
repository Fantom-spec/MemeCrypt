from PIL import Image
import os
def form(path):
    with Image.open(path) as img:
        if img.format!="PNG":
            filename=os.path.splitext(path)[0]
            output=f"{filename}.png"
            if img.mode in ("RGBA","P"):
                img=img.convert("RGB")
            img.save(output,"PNG")
