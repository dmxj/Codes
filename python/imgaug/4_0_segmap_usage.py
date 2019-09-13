# -*- coding: utf-8 -* -
"""
语义分割或实体分割的segmentation map根据图像变换随之变换
"""
import imgaug as ia
from imgaug import augmenters as iaa
import imageio
import numpy as np

ia.seed(1)

# Load an example image (uint8, 128x128x3).
image = ia.quokka(size=(128, 128))

# Create an example segmentation map (int32, 128x128).
# Here, we just randomly place some squares on the image.
# Class 0 is the background class.
segmap = np.zeros((128, 128), dtype=np.int32)
segmap[28:71, 35:85] = 1
segmap[10:25, 30:45] = 2
segmap[10:25, 70:85] = 3
segmap[10:110, 5:10] = 4
segmap[118:123, 10:110] = 5
segmap = ia.SegmentationMapOnImage(segmap, shape=image.shape, nb_classes=1+5)

# Define our augmentation pipeline.
seq = iaa.Sequential([
    iaa.Dropout([0.05, 0.2]),      # drop 5% or 20% of all pixels
    iaa.Sharpen((0.0, 1.0)),       # sharpen the image
    iaa.Affine(rotate=(-45, 45)),  # rotate by -45 to 45 degrees (affects heatmaps)
    iaa.ElasticTransformation(alpha=50, sigma=5)  # apply water effect (affects heatmaps)
], random_order=True)

# Augment images and heatmaps.
images_aug = []
segmaps_aug = []
for _ in range(5):
    seq_det = seq.to_deterministic()
    images_aug.append(seq_det.augment_image(image))
    segmaps_aug.append(seq_det.augment_segmentation_maps([segmap])[0])

# We want to generate an image of original input images and heatmaps before/after augmentation.
# It is supposed to have five columns: (1) original image, (2) augmented image,
# (3) augmented heatmap on top of augmented image, (4) augmented heatmap on its own in jet
# color map, (5) augmented heatmap on its own in intensity colormap,
# We now generate the cells of these columns.
#
# Note that we add a [0] after each heatmap draw command. That's because the heatmaps object
# can contain many sub-heatmaps and hence we draw command returns a list of drawn sub-heatmaps.
# We only used one sub-heatmap, so our lists always have one entry.
cells = []
for image_aug, segmap_aug in zip(images_aug, segmaps_aug):
    cells.append(image)                                      # column 1
    cells.append(segmap.draw_on_image(image))                # column 2
    cells.append(image_aug)                                  # column 3
    cells.append(segmap_aug.draw_on_image(image_aug))        # column 4
    cells.append(segmap_aug.draw(size=image_aug.shape[:2]))  # column 5

# Convert cells to grid image and save.
grid_image = ia.draw_grid(cells, cols=5)
imageio.imwrite("example_segmaps.jpg", grid_image)


