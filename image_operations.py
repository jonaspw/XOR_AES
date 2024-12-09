from PIL import Image
import io

def load_image(file_path):
    # Funkcja wczytująca obraz z pliku.
    with open(file_path, 'rb') as file:
        image_bytes = file.read()
    return image_bytes

def save_image(image_bytes, file_path):
    # Funkcja zapisująca obraz do pliku.
    with open(file_path, 'wb') as file:
        file.write(image_bytes)

def is_valid_image(image_bytes):
    # Funkcja sprawdzająca, czy dane są poprawnym obrazem.
    try:
        Image.open(io.BytesIO(image_bytes))
        return True
    except:
        return False
