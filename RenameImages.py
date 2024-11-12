import os

# Folder path
folder_path = 'PEKTUS EKSKAVATUM'
rename_factor = 'pektus ekskavatum'

start_number = 0

# Rename each image in a folder
for i, filename in enumerate(os.listdir(folder_path), start=start_number):
    file_extension = os.path.splitext(filename)[1]

    new_filename = f"{rename_factor}_{i}{file_extension}"

    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)

    os.rename(old_file, new_file)
    print(f"{filename} yeniden adlandırıldı -> {new_filename}")

print("Tüm dosyalar yeniden adlandırıldı.")
