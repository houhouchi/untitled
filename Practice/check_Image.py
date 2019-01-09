#coding=utf-8
from PIL import Image
img = Image.open('/Users/linran/Desktop/WechatIMG76.jpeg')
print(img.format,img.size,img.mode)