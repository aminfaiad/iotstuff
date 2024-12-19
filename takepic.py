import cv2
import os
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

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

# Wait for 1 second before capturing the next image
time.sleep(1)

# Capture the second frame
ret, frame = cap.read()
if ret:
    # Define the filename for the second image
    filename2 = os.path.join(os.getcwd(), 'captured_image_2.jpg')
    # Save the captured image
    cv2.imwrite(filename2, frame)
    print(f"Second image captured and saved to {filename2}")
else:
    print("Error: Failed to capture the second image.")

# Wait for 1 more second before capturing the third image
time.sleep(1)

# Capture the third frame
ret, frame = cap.read()
if ret:
    # Define the filename for the third image
    filename3 = os.path.join(os.getcwd(), 'captured_image_3.jpg')
    # Save the captured image
    cv2.imwrite(filename3, frame)
    print(f"Third image captured and saved to {filename3}")
else:
    print("Error: Failed to capture the third image.")

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
