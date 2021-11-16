import cv2.cv2 as cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.png', 0)
template = cv2.imread('target.png', 0)

w, h = template.shape[:2]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

left_top = max_loc
right_bottom = (left_top[0] + w, left_top[1] + h)

cv2.rectangle(img, left_top, right_bottom, 255, 2)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('Detected Point \nleft_top:' + str(left_top) + '\nright_bottom:' + str(right_bottom))
plt.xticks([])
plt.yticks([])

plt.show()
