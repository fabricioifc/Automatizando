import argparse
import os
from pathlib import Path
from tqdm import tqdm
import magic
from PIL import Image, ImageColor
import numpy as np
import cv2
import matplotlib.pyplot as plt
import shutil
import enum

class OP(enum.Enum):
    MOVE = 'move'
    DELETE = 'delete'

"""
Função criada para percorrer uma pasta com imagens TIFF RGB e 
remover as imagens que possuem mais que 50% de pixels pretos".

How to Execute
# python main.py --label_dir='/home/fabricio/Mauren/images/mata/slices/256/'
"""
class RemoveImagePixelColor():

    ignored_folders = ['moved']

    def __init__(self, label_dir, percent=0.5) -> None:
        assert os.path.exists(label_dir), "{} don't exists".format(label_dir)
        self.label_dir = label_dir
        self.percent = percent
        
    def run(self, op: OP, color: dict) -> None:
        progress = tqdm(total=self.__count_total(self.label_dir))

        for root, _, files in os.walk(self.label_dir):
            if os.path.basename(root) in self.ignored_folders:
                continue

            for name in files:
                if self.__check_is_png(os.path.join(root, name)) is True:
                    file_path = os.path.join(root, name)
                    input_file = os.path.splitext(file_path)[0] + ".png"

                    # Abrir a imagen original em formato RGB                    
                    image = Image.open(input_file)
                    image = image.convert('RGB')
                    
                    # Percorrer cada pixel da imagem
                    can_move = self.__check_image_predominant_color(image, color)

                    # Caso a imagem não possua mais que 50% de pixels pretos, remover a imagem
                    if can_move:
                        if op == OP.DELETE:
                            progress.set_description(f"Deleting {name}")
                            os.remove(input_file)
                        elif op == OP.MOVE:
                            progress.set_description(f"Moving {name}")
                            # create moved folder if not exists
                            os.makedirs(os.path.join(root, 'moved'), exist_ok=True)
                            shutil.move(file_path, os.path.join(root, 'moved', name))
                            # os.remove(input_file)
                        else:
                            raise ValueError('Invalid type')
                    
                    progress.update(1)
        progress.close()

    def __check_is_png(self, filepath: str) -> bool:
        allowed_types = [
            'image/png',
        ]

        if magic.from_file(filepath, mime=True) not in allowed_types:
            return False
        return True
    
    def __check_image_predominant_color(self, image: Image, color: dict) -> bool:
        pixels = image.load()
        width, height = image.size

        total_pixels = width * height
        total_color_pixels = 0

        for i in range(width):
            for j in range(height):
                if pixels[i,j] == color:
                    total_color_pixels += 1

        if total_color_pixels / total_pixels > self.percent:
            return True
        return False
    
    def __count_total(self, path: str) -> int:
        print('Please wait till total files are counted...')
        # print(path)

        result = 0

        for root, _, files in os.walk(path):
            if os.path.basename(root) in self.ignored_folders:
                continue
            for name in files:
                if self.__check_is_png(os.path.join(root, name)) is True:
                    result += 1

        return result