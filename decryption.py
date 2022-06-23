from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib


def decrypt_blob(encrypted_blob, private_key):
    flag = True
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    try:
        encrypted_blob = base64.b64decode(encrypted_blob)
    except Exception as e:
        print(e)
        print("Decoding Error !!")
        return encrypted_blob, False

    chunk_size = 512
    offset = 0
    decrypted = b""

    while offset < len(encrypted_blob):
        chunk = encrypted_blob[offset:offset + chunk_size]
        try:
            decrypted += rsakey.decrypt(chunk)
        except ValueError as e:
            print(e)
            print("Couldn't decrypt this image :(")
            flag = False
            return encrypted_blob, flag

        offset += chunk_size

    return zlib.decompress(decrypted), flag


def img_decrypt(location):
    print("Reading Private Key ....")
    fd = open("private_key.pem", "rb")
    private_key = fd.read()
    fd.close()

    fd = open("downloaded_images/" + location, "rb")
    encrypted_blob = fd.read()
    fd.close()

    print("Decrypting the image ....")
    unencrypted_blob, flag = decrypt_blob(encrypted_blob, private_key)

    fd = open("decrypted_images/" + location, "wb")
    fd.write(unencrypted_blob)
    fd.close()

    return flag
