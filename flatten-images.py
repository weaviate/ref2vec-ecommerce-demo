import os
import time
from PIL import Image

for root, dirs, file_list in os.walk("./static/old-images"):
    if len(file_list) > 0:
        for file_path in file_list:
            if ".DS_Store" not in file_path:
                filename = file_path.replace(".jpg", "").split("/")[-1]
                image = Image.open(root+"/"+file_path)
                image.save(f"./static/images/{file_path}")