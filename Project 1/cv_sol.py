import numpy as np
import cv2 as cv
import scipy
from PIL import Image
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage.filters import sobel
from skimage import exposure

filename = 'coin_0_1000x750.jpg'
img = Image.open(filename)
plt.imshow(img)
plt.show()
np.set_printoptions(threshold=np.inf)
print(np.array(img))
filename = 'coin_0_1000x750.jpg'
img = cv.imread(filename)
plt.imshow(img)
plt.show()

# assert img is not None, "file could not be read, check with os.path.exists()"
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
# # Rescaling intensity with linear transformation into the range of 0 - 255
#
#
# coin_0_arr = exposure.rescale_intensity(np.array(img))
#
# # Clipping underused values at the end of the exposure scale for better contrast
# # Minor information loss
# v_min, v_max = np.percentile(coin_0_arr, (0.2, 99.8))
#
# coin_0_arr = exposure.rescale_intensity(
#     coin_0_arr, in_range=(v_min, v_max))
#
# markers = np.zeros_like(coin_0_arr)
# markers[coin_0_arr < 30] = 1
# markers[coin_0_arr > 150] = 2
#
# print(markers)
#
# elevation_map = sobel(coin_0_arr)
# plt.imshow(elevation_map)
# plt.show()
#
# img = elevation_map
# # noise removal
# kernel = np.ones((3, 3), np.uint8)
# opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
# # sure background area
# sure_bg = cv.dilate(opening, kernel, iterations=3)
# # Finding sure foreground area
# dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
# ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv.subtract(sure_bg, sure_fg)
#
# # Marker labelling
# ret, markers = cv.connectedComponents(sure_fg)
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers + 1
# # Now, mark the region of unknown with zero
# markers[unknown == 255] = 0
#
# markers = cv.watershed(cv.imread(filename), markers)
# img[markers == -1] = [255, 0, 0]
#
# img = cv.convertScaleAbs(img)
#
# plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB), cmap='jet')
# plt.show()
