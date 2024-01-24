import cv2

# src = cv2.imread('man.jpg', 1)
# src = cv2.imread('crab.png', 1)
src = cv2.imread('angel.png', cv2.IMREAD_UNCHANGED)
_, mask = cv2.threshold(src[:, :, 3], 0, 255, cv2.THRESH_BINARY)

inverted_mask = cv2.bitwise_not(mask)

# show
cv2.imshow('mask', mask)
cv2.waitKey(0)

cv2.imshow('inverted mask', inverted_mask)
cv2.waitKey(0)

# save
cv2.imwrite('inverted_mask.png', inverted_mask)
cv2.destroyAllWindows()