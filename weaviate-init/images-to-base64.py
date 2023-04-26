import os
import time

os.mkdir("base64_images")

start = time.time()
counter = 0

for root, dirs, file_list in os.walk("../static/images"):
    if len(file_list) > 0:
        for file_path in file_list:
            if ".DS_Store" not in file_path:
                filename = file_path.replace(".jpg", "").split("/")[-1]
                os.system("cat " + root + "/" + file_path + " | base64 > base64_images/" + filename + ".txt")
                counter += 1

print(f"Created {counter}  base64 images in: {int(time.time() - start)} seconds.")