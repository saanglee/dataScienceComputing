# PIL: Python Imaging Library

from PIL import ImageFilter
from PIL import Image

def teleport():
  img = Image.open('chocolate.jpg')
  size = (img.size[0] // 10, img.size[1] // 10) # 이미지 크기를 1/10로 줄임
  

  img = img.resize(size) # 이미지 크기 조정
  