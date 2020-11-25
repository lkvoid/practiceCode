# -*- coding=utf-8 -*-

from PIL import Image
import argparse
# 首先，构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

parser.add_argument('filename')
file = parser.parse_args()
im = Image.open(file.filename)


print(im.getpixel((1,3)))


#  txt += get_char(*im.getpixel((j,i)))