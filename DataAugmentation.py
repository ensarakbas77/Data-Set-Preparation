from PIL import Image, ImageEnhance, ImageColor, ImageFilter, UnidentifiedImageError
import os

# Folders (input&output folders)
input_folder = 'pectus excavatum_images_resized'
output_folder = 'PEKTUS EKSKAVATUM'
os.makedirs(output_folder, exist_ok=True)

# Images processing & data augmentation
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_folder, filename)

        try:
            image = Image.open(image_path).convert('RGB')

            img_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor('white', 'RGB'))
            img_rotate.save(os.path.join(output_folder, f"{filename.split('.')[0]}_rotated.jpg"))

            img_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img_horizontal.save(os.path.join(output_folder, f"{filename.split('.')[0]}_flipped.jpg"))

            img_transverse = image.transpose(Image.Transpose.TRANSVERSE)
            img_transverse.save(os.path.join(output_folder, f"{filename.split('.')[0]}_transverse.jpg"))

            black_and_white = image.convert("L")
            black_and_white.save(os.path.join(output_folder, f"{filename.split('.')[0]}_bw.jpg"))

            brightness_enhancer = ImageEnhance.Brightness(image)
            brighter_image = brightness_enhancer.enhance(1.2)
            brighter_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_bright.jpg"))

            color_enhancer = ImageEnhance.Color(image)
            color_image = color_enhancer.enhance(3)
            color_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_color.jpg"))

            contrast_enhancer = ImageEnhance.Contrast(image)
            contrast_image = contrast_enhancer.enhance(2)
            contrast_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_contrast.jpg"))

            sharpness_enhancer = ImageEnhance.Sharpness(image)
            sharp_image = sharpness_enhancer.enhance(6)
            sharp_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_sharp.jpg"))

            filtered_image = image.filter(ImageFilter.DETAIL)
            filtered_image.save(os.path.join(output_folder, f"{filename.split('.')[0]}_filtered.jpg"))

            print(f"{filename} için veri artırma işlemleri tamamlandı.")

        except UnidentifiedImageError:
            print(f"{filename} işlenemedi: Bu dosya geçerli bir resim değil veya bozuk.")
