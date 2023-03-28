import cv2
import time

# Set up camera
cap = cv2.VideoCapture(0)

# Define file name and extension
file_name = "image"
file_ext = ".jpg"

# Define interval in seconds
interval = 5

# Initialize timer
prev_time = time.time()

# Continuously capture images
while True:
    # Get current time
    curr_time = time.time()

    # Check if interval has elapsed
    if curr_time - prev_time >= interval:
        # Reset timer
        prev_time = curr_time

        # Capture image
        ret, frame = cap.read()

        # Save image
        file_path = file_name + str(int(curr_time)) + file_ext
        cv2.imwrite(file_path, frame)

        # Show image
        cv2.imshow('frame',frame)
        
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
