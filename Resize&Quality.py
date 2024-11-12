from PIL import Image, ImageEnhance, ImageFilter, UnidentifiedImageError
import os

# Folders (input&output folders)
input_folder = 'pectus excavatum_images'
output_folder = 'pectus excavatum_images_resized'
os.makedirs(output_folder, exist_ok=True)

# Size of resizing
new_size = (256, 256)

# Image processing and quality enhancement
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):    # Only jpg ve png format
        image_path = os.path.join(input_folder, filename)

        try:
            image = Image.open(image_path).convert('RGB')

            img_resized = image.resize(new_size)

            enhancer = ImageEnhance.Sharpness(img_resized)
            enhanced_image = enhancer.enhance(2.0)

            final_image = enhanced_image.filter(ImageFilter.DETAIL)

            # Save processed image
            output_path = os.path.join(output_folder, f"enhanced_resized_{filename}")
            final_image.save(output_path)
            print(f"{filename} başarıyla işlenip kaydedildi.")

        except UnidentifiedImageError:
            print(f"{filename} işlenemedi: Bu dosya geçerli bir resim değil veya bozuk.")
        except Exception as e:
            print(f"{filename} işlenirken hata oluştu: {e}")
