# -*- coding: utf-8 -* -
from skimage import data

if __name__ == "__main__":
    print(dir(data))
    camera_data = data.camera()
    print(len(camera_data))
    print(len(camera_data[0]))