# -*- coding: utf-8 -* -
"""

"""
import imgaug as ia
import imageio
import numpy as np

# Load an example image (uint8, 128x128x3).
image = ia.quokka(size=(128, 128), extract="square")

# Create an example segmentation map (int32, 128x128).
# Here, we just randomly place some squares on the image.
# Class 0 is the background class.
segmap = np.zeros((128, 128), dtype=np.int32)
segmap[28:71, 35:85] = 1
segmap[10:25, 30:45] = 2
segmap[10:25, 70:85] = 3
segmap[10:110, 5:10] = 4
segmap[118:123, 10:110] = 5
segmap1 = ia.SegmentationMapOnImage(segmap, shape=image.shape, nb_classes=1+5)

# Read out the segmentation map's array, change it and create a new segmentation map
arr = segmap1.get_arr_int()
arr[10:110, 5:10] = 5
segmap2 = ia.SegmentationMapOnImage(arr, shape=image.shape, nb_classes=1+5)

# Draw three columns: (1) original image, (2) original image with unaltered segmentation
# map on top, (3) original image with altered segmentation map on top
cells = [
    image,
    segmap1.draw_on_image(image),
    segmap2.draw_on_image(image)
]

# Convert cells to grid image and save.
grid_image = ia.draw_grid(cells, cols=3)
imageio.imwrite("example_segmaps_array.jpg", grid_image)

