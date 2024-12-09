import random
import time
from xor_cipher import encrypt, decrypt
from image_operations import load_image, save_image, is_valid_image
from aes_cipher import encrypt_aes, decrypt_aes
from Crypto.Random import get_random_bytes

def generate_key_from_password(password):
    # Zamień każdy znak hasła na jego kod ASCII, a następnie zsumuj je, aby uzyskać klucz.
    return sum(map(ord, password)) % 256

def save_execution_time(start_time, end_time, operation_type):
    # Zapisz czas wykonania operacji do pliku.
    with open('execution_time.txt', 'a') as file:
        file.write(f"Czas {operation_type}: {end_time - start_time} sekund.\n")

def generate_random_key():
    # Funkcja generująca klucz pseudolosowy z zakresu 0-255.
    return random.randint(0, 255)

def save_key_to_file(key, file_path):
    # Funkcja zapisująca klucz do pliku.
    with open(file_path, 'w') as file:
        file.write(str(key))

def save_keys_to_file(keys, valid_keys, file_path):
    # Funkcja zapisująca listę kluczy do pliku z oznaczeniem poprawności.
    with open(file_path, 'w') as file:
        for key in keys:
            is_valid = "Poprawny" if key in valid_keys else "Niepoprawny"
            file.write(f"{key}: {is_valid}\n")

def main():
    # Ścieżki do plików
    input_image_path = 'IMG11.jpeg'
    encrypted_image_path = 'encrypted_image.jpg'
    decrypted_image_path = 'decrypted_image.jpg'
    decrypted_image_path_aes = 'decrypted_image_aes.jpg'
    encrypted_image_path_aes = 'encrypted_image_aes.jpg'
    key_file_path = 'key.txt'
    key_file_path_aes = 'key_aes.txt'
    brute_force_keys_file_path = 'brute_force_keys.txt'

    # Czyszczenie pliku z czasami wykonania
    with open('execution_time.txt', 'w') as file:
        file.truncate()

    # Wybór użycia hasła
    print("Czy chcesz użyć hasła? (tak/nie):")
    use_password = input().lower()

    if use_password == "tak":
        print("Podaj hasło:")
        password = input()
        key = generate_key_from_password(password)
    else:
        key = generate_random_key()

    # Wczytanie obrazu
    image_bytes = load_image(input_image_path)

    start_time_encoding = time.time()  # Początek mierzenia czasu kodowania

    # Szyfrowanie obrazu
    encrypted_bytes = encrypt(image_bytes, key)
    save_image(encrypted_bytes, encrypted_image_path)
    print("Obraz został zaszyfrowany kluczem:", key)

    # Zapisz klucz do pliku
    save_key_to_file(key, key_file_path)

    end_time_encoding = time.time()  # Koniec mierzenia czasu kodowania
    print("Czas szyfrowania wyniósł ", end_time_encoding - start_time_encoding, "sekund.")

    start_time_decoding = time.time()  # Początek mierzenia czasu odkodowywania

    # Deszyfrowanie obrazu (metoda brute-force)
    brute_force_keys = []
    valid_keys = []
    print("Trwa deszyfrowanie obrazu...")
    for possible_key in range(256):
        decrypted_bytes = decrypt(encrypted_bytes, possible_key)
        brute_force_keys.append(possible_key)
        print(possible_key)

        # Sprawdzenie poprawności deszyfrowania
        if is_valid_image(decrypted_bytes):
            save_image(decrypted_bytes, decrypted_image_path)
            print(f"Obraz zdeszyfrowany poprawnym kluczem: {possible_key}")
            valid_keys.append(possible_key)
            break

    end_time_decoding = time.time()  # Koniec mierzenia czasu odkodowywania
    print("Czas deszyfrowania wyniósł ", end_time_decoding - start_time_decoding, "sekund.")

    # Zapisz listę kluczy z bruteforce do pliku
    save_keys_to_file(brute_force_keys, valid_keys, brute_force_keys_file_path)

    # Zapisz czasy wykonania operacji
    save_execution_time(start_time_encoding, end_time_encoding, "kodowania")
    save_execution_time(start_time_decoding, end_time_decoding, "odkodowywania")

    # Użycie AES do szyfrowania i odszyfrowywania obrazu
    print("Czy chcesz użyć AES do szyfrowania i odszyfrowywania obrazu? (tak/nie):")
    use_aes = input().lower()

    if use_aes == "tak":
        aes_key = get_random_bytes(16)  # Użyj klucza o długości 16 bajtow (128)bitów
        save_key_to_file(aes_key, key_file_path_aes)


        # Szyfruj obraz za pomocą AES
        image_bytes_aes = load_image(input_image_path)
        start_time_aes_encryption = time.time()
        encrypted_bytes_aes = encrypt_aes(image_bytes_aes, aes_key)
        end_time_aes_encryption = time.time()
        save_image(encrypted_bytes_aes, encrypted_image_path_aes)
        print("Czas szyfrowania AES wyniósł ", end_time_aes_encryption - start_time_aes_encryption, "sekund.")

        # Odszyfruj obraz za pomocą AES
        image_bytes_aes = load_image(encrypted_image_path_aes)
        start_time_aes_decryption = time.time()
        decrypted_bytes_aes = decrypt_aes(image_bytes_aes, aes_key)
        end_time_aes_decryption = time.time()
        save_image(decrypted_bytes_aes, decrypted_image_path_aes)

        print("Czas deszyfrowania AES wyniósł ", end_time_aes_decryption - start_time_aes_decryption, "sekund.")

        # Zapisz czasy wykonania operacji AES
        save_execution_time(start_time_aes_encryption, end_time_aes_encryption, "kodowania AES")
        save_execution_time(start_time_aes_decryption, end_time_aes_decryption, "odkodowywania AES")

# Sprawdzenie czy program jest uruchamiany jako główny program
if __name__ == "__main__":
    main()
