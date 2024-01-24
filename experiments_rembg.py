import cv2
import rembg

# src = cv2.imread('man.jpg', 1)
src = cv2.imread('crab.png')

output = rembg.remove(
    src,
    session=rembg.new_session('isnet-general-use'),
    only_mask=True
)

#dst = cv2.bitwise_not(output)
cv2.imwrite('output_mask_inverted.jpg', output)
