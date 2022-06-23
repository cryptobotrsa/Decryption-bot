from decryption import img_decrypt
from download_images import download_from_drive
import os

download_folder = "downloaded_images"
files = os.listdir(download_folder)
for file in files:
    os.remove(download_folder + "/" + file)

download_from_drive(download_folder)

files = os.listdir(download_folder)
img_files = []
for file in files:
    if file[-4::1] == '.jpg':
        img_files.append(file)

i = 0
for image in img_files:
    i = i + 1
    print("\nAnalyzing the encrypted image .... " + image + " ....  (" + str(i) + "/" + str(len(img_files)) + ")")
    flag = img_decrypt(image)
    if flag:
        print("Decryption Successful !! ......... " + image + " ....  (" + str(i) + "/" + str(len(img_files)) + ")")


