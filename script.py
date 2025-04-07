from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # gri ton

def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = "```\n"

    for row in pixels:
        for pixel in row:
            index = int(pixel / 255 * (len(ASCII_CHARS) - 1))
            ascii_str += ASCII_CHARS[index]
        ascii_str += "\n"

    ascii_str += "```"
    return ascii_str



def main(image_path):
    try:
        image = Image.open(image_path)
    except:
        print("Görsel açılamadı.")
        return

    image = resize_image(image)
    gray_image = grayify(image)
    ascii_str = pixels_to_ascii(gray_image)

    with open("ascii_output.txt", "w", encoding="utf-8") as f:
        f.write(ascii_str)

    print("ASCII çıktı başarıyla oluşturuldu. → ascii_output.txt")

if __name__ == "__main__":
    path = input("Görsel yolunu girin (örnek: image.jpg): ")
    main(path)
