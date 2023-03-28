import cv2
import numpy as np

# Load image
img = cv2.imread('captured_image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to remove noise
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Invert image to make text black
thresh = 255 - thresh

# Dilate image to make text thicker
kernel = np.ones((2,2), np.uint8)
thresh = cv2.dilate(thresh, kernel, iterations=1)

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour that corresponds to the middle line of the book
# This assumes that the two pages are equally sized and the spine of the book is in the middle of the image
middle_contour = None
min_dist = float('inf')
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    if h > img.shape[0] / 2 and w < img.shape[1] / 4:
        # Compute distance from center of image
        dist = abs(x + w/2 - img.shape[1]/2)
        if dist < min_dist:
            min_dist = dist
            middle_contour = contour

# Split the image into two separate images
x,y,w,h = cv2.boundingRect(middle_contour)
left_img = img[0:img.shape[0], 0:x+w//2]
right_img = img[0:img.shape[0], x+w//2:img.shape[1]]

# Save the left and right images
cv2.imwrite('left_page.jpg', left_img)
cv2.imwrite('right_page.jpg', right_img)

# Display the left and right images
cv2.imshow('Left Page', left_img)
cv2.imshow('Right Page', right_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
