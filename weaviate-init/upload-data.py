import weaviate
from weaviate.util import get_valid_uuid
from uuid import uuid4
import time
import os
import pandas as pd
import chardet

client = weaviate.Client("http://localhost:8080")

# get labelName - properties dict
imagePath_sku = {}
sku_imagepath_dir = "./metadata/sku-imgpath"
for filename in os.listdir(sku_imagepath_dir):
    df = pd.read_csv(sku_imagepath_dir+"/"+filename)
    for index, row in df.iterrows():
        image_path = row["image"].replace(".jpg", "").split("/")[-1]
        imagePath_sku[image_path] = row["sku"]

# sku --> {"category", "qty", "price", ...}
sku_metadata = {}
sku_metadata_dir = "./metadata/metadata"
for filename in os.listdir(sku_metadata_dir):
    with open(sku_metadata_dir+"/"+filename, 'rb') as f:
        result = chardet.detect(f.read())
        df = pd.read_csv(sku_metadata_dir+"/"+filename, encoding=result['encoding'])

        for index, row in df.iterrows():
            sku_metadata[row["sku"]] = {
                "category": row["category"],
                "name": row["name"],
                "price": row["price"],
                "qty": row["qty"],
                "description": row["description"]
            }

counter = 0
start = time.time()
for encoded_file_path in os.listdir("./base64_images"):
    f = open("./base64_images/"+encoded_file_path)
    base64_encoding = f.readlines()
    base64_encoding = ' '.join(base64_encoding)
    base64_encoding = base64_encoding.replace("\n", "").replace(" ", "")

    imagePath = encoded_file_path.replace(".txt", "")

    if imagePath in imagePath_sku.keys():
        sku = imagePath_sku[imagePath]
        if sku in sku_metadata.keys():
            metadata = sku_metadata[sku]

            data_properties = {
                "labelName": imagePath,
                "image": base64_encoding,
                "index": counter,
                "sku": sku,
                "category": metadata["category"],
                "name": metadata["name"],
                "price": metadata["price"],
                "qty": metadata["qty"],
                "description": metadata["description"]
            }
    else:
        data_properties = {
            "labelName": imagePath,
            "image": base64_encoding,
            "index": counter,
        }

    id = get_valid_uuid(uuid4())
    counter += 1

    client.data_object.create(data_properties, "Product", id)
    f.close()

print(f"Uploaded: {counter} images in {int(time.time() - start)} seconds.")
