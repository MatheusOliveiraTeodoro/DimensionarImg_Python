import os
import re
from PIL import Image


def calc_new_height(width, height, new_width):
    return round(new_width * height / width)


def resize(root, file, new_width, new_img_name):
    original_img_path = os.path.join(root, file)
    new_img_path = os.path.join(root, new_img_name)

    pillow_img = Image.open(original_img_path)
    width, height = pillow_img.size

    new_height = calc_new_height(width, height, new_width)

    # Redimensiona a imagem
    new_img = pillow_img.resize((new_width, new_height), Image.LANCZOS)

    # Salva sem EXIF
    new_img.save(
        new_img_path,
        optimize=True,
        quality=50
    )

    print(f'Saved at {new_img_path}')


def is_image(extension):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))


def files_checks(root, file):
    filename, extension = os.path.splitext(file)

    
    if not is_image(extension):
        return

    flag = '_CONVERTED'

    
    if flag in file:
        return

    new_img_name = filename + flag + extension

    
    resize(root=root, file=file, new_width=1920, new_img_name=new_img_name)


def files_loop(root, files):
    for file in files:
        files_checks(root, file)


def main(root_folder):
    for root, dirs, files in os.walk(root_folder):
        files_loop(root, files)


if __name__ == '__main__':
    root_folder = '/home/ubuntuUser/Documents/fotos-ecommerce-20241127T145626Z-001/fotos-ecommerce'
    main(root_folder)
