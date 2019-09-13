import cv2

def im_read(img_path):
    im = cv2.imread(img_path)

    print(im.shape)

if __name__ == '__main__':
    im_read("./imgs/img1.jpg")


