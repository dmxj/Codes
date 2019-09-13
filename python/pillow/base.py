# -*- coding: utf-8 -* -
from PIL import Image, ImageFilter


def get_img_info():
    '''
    获取图片信息（格式、宽高、模式）
    :return:
    '''
    im = Image.open("cluo.jpg")

    # 输出：JPEG 宽高(499, 333) RGB
    print(im.format, im.size, im.mode)


def show_img():
    '''
    显示图片
    :return:
    '''
    im = Image.open("cluo.jpg")
    im.show()


def thum_img():
    '''
    获取图片的宽和高，并缩放50%
    :return:
    '''
    im = Image.open("cluo.jpg")
    # 获得图片宽高
    width, height = im.size

    # 将图片缩放到50%（im本身改变了）
    im.thumbnail((width // 2, height // 2))

    # 将缩放后的图片保存到本地
    im.save("result/cluo_thumbnail.jpg")


def gray_img():
    '''
    灰度变换
    :return:
    '''
    im = Image.open("cluo.jpg").convert("L")


def rotate_img():
    '''
    旋转、翻转
    :return:
    '''
    im = Image.open("cluo.jpg")
    # 旋转45度
    out = im.rotate(45)
    # 图片翻转
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out = im.transpose(Image.FLIP_TOP_BOTTOM)
    # 图片旋转
    out = im.transpose(Image.ROTATE_90)
    out = im.transpose(Image.ROTATE_180)
    out = im.transpose(Image.ROTATE_270)


def crop_rect_from_img():
    '''
    从图像中复制出一个矩形选区
    :return:
    '''
    im = Image.open("cluo.jpg")

    # box 4个元素分别代表左、上、右、下的坐标，以左上角为坐标原点，单位px
    box = (100, 100, 400, 400)
    region = im.crop(box)

    # 旋转区域
    region = region.transpose(Image.ROTATE_180)

    # 按照box的坐标将复制出来的区域粘贴回原区域
    im.paste(region, box)


def reorder_img_channel():
    '''
    重新整合图像颜色通道
    :return:
    '''
    im = Image.open("cluo.jpg")
    # 图像默认的通道：r,g,b
    r, g, b = im.split()
    # 此时的im通道顺序：b,g,r
    im = Image.merge("RGB", (b, g, r))


def blur_img():
    '''
    模糊滤镜
    :return:
    '''
    im = Image.open("cluo.jpg")
    # 应用模糊滤镜
    im2 = im.filter(ImageFilter.BLUR)

    # 保存模糊后的图片
    im2.save("result/cluo_blur.jpg", 'jpeg')

if __name__ == "__main__":
    get_img_info()





