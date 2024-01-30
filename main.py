import argparse
import os
from pathlib import Path
from tqdm import tqdm
import magic
from PIL import Image, ImageColor
import numpy as np
from lib.remove_image_pixel_color import RemoveImagePixelColor
from lib.remove_image_pixel_color import OP

def tuple_from_string(s):
    return tuple(map(int, s.strip('()').split(',')))
    
if __name__ == '__main__':
    # How to Execute
    # python main.py --label_dir='lib/samples/' --percent=0.5 --color='(0, 0, 0)' --op='move'
    parser = argparse.ArgumentParser(description='Remove slices with a lot of black pixels')
    parser.add_argument('--percent', type=float, help='Percent of black pixels', default=0.5)
    parser.add_argument('--label_dir', type=str, help='Path do directory with tif images')
    parser.add_argument('--color', type=tuple_from_string, help='Pixel Color', default=(0, 0, 0))
    parser.add_argument('--op', type=OP, help='Type of action', default=OP.MOVE)
    args = parser.parse_args()
    
    RemoveImagePixelColor(args.label_dir, args.percent).run(args.op, args.color)