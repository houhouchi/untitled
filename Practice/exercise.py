#coding=utf-8
from PIL import Image
from time import sleep
#读取图片
img = Image.open('/Users/linran/Desktop/马8450.jpg')
生成缩略图
img.thumbnail((100,100))
#缩放图片为50*50
img.resize((50,50))
#保存图片
img.save('qq_image_thumb.jpg','JPEG')
#输出图片的格式、尺寸、图像类型
print(img.format,img.size,img.mode)
#显示图片
img.show()
#逆时针旋转45度
# rotate1 = img.rotate(45)
# rotate1.show()
# sleep(10)
#逆时针旋转90度，只有选择90、180、270度的时候、用img.transpose(Image.ROTATE_90)
#其他佳都用img.ratte(度数)
rotate2 = img.transpose(Image.ROTATE_90)
rotate2.show()
#左右对换
rotate3 = img.transpose(Image.FLIP_LEFT_RIGHT)
rotate3.show()

#上下翻转
rotate4 = img.transpose(Image.FLIP_TOP_BOTTOM)
rotate4.show()

# '''
# 裁剪，逆时针旋转，粘贴
#
# '''
# box = (200,200,400,400) #裁剪范围（左，上，右，下）
# region = img.corp(box)
# region.show()
# region1 = region.transpose(Image.ROTATE_180)#旋转180度
# region1.show()
# img.paste(region1,box)
# img.show()

