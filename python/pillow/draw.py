# -*- coding: utf-8 -* -
from PIL import Image, ImageDraw, ImageFont


def draw_rect(img_path):
    '''
    绘制一个红色的矩形（填充的）
    :param img_path: 图片路径
    :return:
    '''
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    draw.rectangle((10,10,150,150),"red")
    im.show()
    del draw


def draw_line_react(img_path):
    '''
    绘制矩形框（中心是空的，相当于绘制四条边线）
    :param img_path:
    :return:
    '''
    x, y = 10, 10
    w, h = 200, 200
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    draw.line((x, y, x + w, y), fill="green", width=4)
    draw.line((x, y, x, y + h), fill="green", width=4)
    draw.line((x, y + h, x + w, y + h), fill="green", width=4)
    draw.line((x + w, y, x + w, y + h), fill="green", width=4)
    im.show()
    del draw


def draw_text(img_path):
    '''
    在图片上绘制文字
    :param img_path:
    :return:
    '''
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font="/Library/Fonts/Microsoft Sans Serif.ttf", size=40, encoding="unic")
    draw.text((20,20), "像C罗一样踢球", fill="green", spacing=1, font=font)
    im.show()
    del draw


if __name__ == "__main__":
    # draw_rect("cluo.jpg")
    draw_line_react("/Users/rensike/Work/宝钢热轧/data_anno_v2/划伤/P4350021_00008979_11_srcimg_0010.tif")
    # draw_text("cluo.jpg")