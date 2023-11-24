from skimage.measure import label, regionprops
from scipy.ndimage import binary_dilation
import cv2

kr = 0

for i in range(1, 13):
    img = cv2.imread(f"images/img ({i}).jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_not(mask)
    mask[mask != 0] = 1
    mask = binary_dilation(binary_dilation(mask))
    mask = label(mask)
    mask = regionprops(mask)

    for i in mask:
        if ((i.image.shape[0] > 1000 and i.image.shape[1] > 50) or (
                i.image.shape[1] > 1000 and i.image.shape[0] > 50)) and i.eccentricity > 0.9:
            kr += 1

print(f"Общее количество карандашей в наборе изображений: {kr}")
