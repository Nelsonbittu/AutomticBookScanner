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

# Find largest contour and draw bounding rectangle
max_contour = max(contours, key=cv2.contourArea)
x,y,w,h = cv2.boundingRect(max_contour)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# Crop image to bounding rectangle
cropped = img[y:y+h, x:x+w]

# Resize image to standard size (optional)
cropped = cv2.resize(cropped, (800, 800))

# Save the processed image
cv2.imwrite('scanned_image.jpg', cropped)

# Display the processed image
cv2.imshow('Scanned Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
