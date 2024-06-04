from PIL import Image, ImageFilter

img = Image.open('')

img.show()
img.filename
img.format # JPEG
img.size # (640, 426)

img.resize((400, 300))
img.crop((0,0,300,300)) # (좌측상단 x, y, 우측하단 x, y)
img.rotate(90) 

img.transpose(Image.FLIP_LEFT_RIGHT)
img.transpose(Image.FLIP_TOP_BOTTOM)

img.save('')

img.convert("L") # 흑백

img.filter(ImageFilter.GaussianBlur(9))
img.filter(ImageFilter.EDGE_ENHANCE)

"""Filters
BLUR: BLUR, BoxBlur(), GaussianBlur()
MedianFilter()
CONTOUR
DETAIL
EDGE_ENHANCE, EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SHARPEN
SMOOTH, SMOOTH_MORE
"""