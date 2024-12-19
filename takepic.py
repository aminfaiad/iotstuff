import cv2
import os
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set the resolution to 2K (2560x1440)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

# Confirm the resolution
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Webcam resolution set to: {width}x{height}")

# Wait for 10 seconds
print("Waiting for 10 seconds before capturing the first image...")
time.sleep(10)

# Capture the first frame
ret, frame = cap.read()
if ret:
    # Define the filename with path for the first image
    filename1 = os.path.join(os.getcwd(), 'captured_image_1.jpg')
    # Save the captured image
    cv2.imwrite(filename1, frame)
    print(f"First image captured and saved to {filename1}")
else:
    print("Error: Failed to capture the first image.")

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
