from PIL import ImageFilter
from PIL import Image

def teleport():
  img = Image.open('chocolate.jpg')
  size = (img.size[0]//10, img.size[1]//10)
  ###code here ###
  
  filter = input("chose filter (1: blur, 2: edge_enhance, 3: emboss, 4: gray) : ")

  img = img.resize(size)
  img = img.transpose(Image.FLIP_LEFT_RIGHT)
  # apply filter
  if filter == '1':
    img = img.filter(ImageFilter.BLUR)
  elif filter == '2':
    img = img.filter(ImageFilter.EDGE_ENHANCE)
  elif filter == '3':
    img = img.filter(ImageFilter.EMBOSS)
  elif filter == '4':
    img = img.convert('L')
  img.save('img.jpeg')

if __name__ =="__teleport__":
  teleport()
  