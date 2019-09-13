# -*- coding: utf-8 -* -
'''
多张图拼接成一张图
'''
from PIL import Image

img_file_lists = ["../../opencv/imgs/img0.jpg","../../opencv/imgs/img1.jpg"]

def cat_imgs():
    ims = [Image.open(img_file) for img_file in img_file_lists]

    total_width = 0
    max_height = 0

    for im in ims:
        width,height = im.size
        total_width += width
        if height > max_height:
            max_height = height

    result = Image.new(ims[0].mode,(total_width,max_height))

    x = 0
    for i,im in enumerate(ims):
        width, height = im.size
        result.paste(im,box=(x,0))
        x += width

    result.show()
    result.save("cat_img_result.jpg")

def cat_imgs_vertical(image_files,dist_file):
    ims = [Image.open(img_file) for img_file in image_files]

    total_height = 0
    max_width = 0

    for im in ims:
        width,height = im.size
        total_height += height
        if width > max_width:
            max_width = width

    result = Image.new(ims[0].mode,(max_width,total_height))

    y = 0
    for i,im in enumerate(ims):
        width, height = im.size
        result.paste(im,box=(0,y))
        y += height
        y += 2

    result.show()
    result.save(dist_file)

if __name__ == '__main__':
    import glob
    import os
    cat_imgs_vertical(glob.glob(os.path.join("/Users/rensike/Files/brother","*.png")),"/Users/rensike/Files/brother/combine.png")

