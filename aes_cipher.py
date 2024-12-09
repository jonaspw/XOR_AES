from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
def encrypt_aes(image_data, key):

    # Inicjalizuj AES z trybem ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Szyfruj dane obrazu
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    return encrypted_data

def decrypt_aes(encrypted_data, key):

    # Inicjalizuj AES z trybem ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Odszyfruj dane obrazu
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data
