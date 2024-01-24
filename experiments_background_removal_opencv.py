import numpy as np
import cv2

# src = cv2.imread('man.jpg', 1)
# src = cv2.imread('crab.png', 1)
src = cv2.imread('angel.png', 1)

######## remove alpha
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Applying thresholding technique
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)

# Using cv2.split() to split channels
# of coloured image
b, g, r = cv2.split(src)

# Making list of Red, Green, Blue
# Channels and alpha
rgba = [b, g, r, alpha]

# Using cv2.merge() to merge rgba
# into a coloured/multi-channeled image
dst = cv2.merge(rgba, 4)

cv2.imshow('alpha', alpha)
cv2.waitKey(0)

cv2.imshow('alpha removed', dst)
cv2.waitKey(0)

######### make mask

ret, mask = cv2.threshold(dst[:, :, 3], 0, 255, cv2.THRESH_BINARY)

cv2.imshow('mask', mask)
cv2.waitKey(0)

# see the results

cv2.imwrite('alpha_removal.png', mask)
cv2.destroyAllWindows()


# # Read image
# img = cv2.imread('pills.jpg')
# hh, ww = img.shape[:2]
# # threshold on white
# # Define lower and uppper limits
# lower = np.array([200, 200, 200])
# upper = np.array([255, 255, 255])
#
# # Create mask to only select black
# thresh = cv2.inRange(img, lower, upper)
#
# # apply morphology
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#
# # invert morp image
# mask = 255 - morph
#
# # apply mask to image
# result = cv2.bitwise_and(img, img, mask=mask)
#
#
# # save results
# cv2.imwrite('pills_thresh.jpg', thresh)
# cv2.imwrite('pills_morph.jpg', morph)
# cv2.imwrite('pills_mask.jpg', mask)
# cv2.imwrite('pills_result.jpg', result)
#
# cv2.imshow('thresh', thresh)
# cv2.imshow('morph', morph)
# cv2.imshow('mask', mask)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()