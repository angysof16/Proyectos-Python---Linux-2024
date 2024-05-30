import os
import argparse
import shutil
import time
from PIL import Image

def organize_photos(source_path, dest_path):
    files = os.listdir(source_path)
    
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    for file in files:
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.avi')):
                creation_time = os.path.getmtime(file_path)
                date_folder = time.strftime('%Y.%m.%d', time.localtime(creation_time))
                
                day_path = os.path.join(dest_path, date_folder)
                if not os.path.exists(day_path):
                    os.makedirs(day_path)
                
                shutil.copy(file_path, day_path)
                
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    thumbs_path = os.path.join(day_path, 'thumbs')
                    if not os.path.exists(thumbs_path):
                        os.makedirs(thumbs_path)
                    img = Image.open(file_path)
                    img.thumbnail((100, 100))
                    img.save(os.path.join(thumbs_path, file))
    
    print("Organización completada.")

def main():
    parser = argparse.ArgumentParser(description='Organizador de fotos')
    parser.add_argument('-s', '--source', type=str, required=True, help='Directorio de origen de las fotos')
    parser.add_argument('-d', '--destination', type=str, required=True, help='Directorio de destino de las fotos organizadas')
    args = parser.parse_args()
    
    source_path = os.path.abspath(args.source)
    dest_path = os.path.abspath(args.destination)
    
    organize_photos(source_path, dest_path)

if __name__ == "__main__":
    main()
