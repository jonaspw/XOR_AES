def encrypt(image_bytes, key):
    # Funkcja szyfrująca obraz za pomocą XOR.
    encrypted_bytes = bytearray()
    for byte in image_bytes:
        encrypted_byte = byte ^ key
        encrypted_bytes.append(encrypted_byte)
    return bytes(encrypted_bytes)

def decrypt(encrypted_bytes, key):
    # Funkcja deszyfrująca obraz za pomocą XOR.
    return encrypt(encrypted_bytes, key)
