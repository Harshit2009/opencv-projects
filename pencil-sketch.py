import cv2
import sys

# read image
image = cv2.imread('./portrait_small.jpg')

# check if image exists
if image is None:
    print("can not find image")
    sys.exit()

# convert to gray scale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# invert the gray image
grayImageInv = 255 - grayImage

# Apply gaussian blur
grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)

# blend using color dodge
output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)

# create windows to dsiplay images
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)

# display images
cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)

# press esc to exit the program
cv2.waitKey(0)

# close all the opened windows
cv2.destroyAllWindows()
