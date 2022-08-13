#!/usr/bin/env python3
from PIL import Image
import os

#path to the images folder
img_path = "supplier-data/images/"

for file in os.listdir(img_path):
  if file.endswith(".tiff"):
    img = Image.open(img_path+file).convert('RGB')
    file_name = os.path.splitext(file)[0]
    img.resize((600, 400)).save("supplier-data/images/" + file_name + ".jpeg", "JPEG")
