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

actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
actual_contrast = cap.get(cv2.CAP_PROP_CONTRAST)
actual_saturation = cap.get(cv2.CAP_PROP_SATURATION)
actual_hue = cap.get(cv2.CAP_PROP_HUE)
actual_gain = cap.get(cv2.CAP_PROP_GAIN)
actual_exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
actual_autofocus = cap.get(cv2.CAP_PROP_AUTOFOCUS)

print("Camera Settings Before Attempted Update:")
print(f" - Resolution     : {actual_width} x {actual_height}")
print(f" - Brightness     : {actual_brightness}")
print(f" - Contrast       : {actual_contrast}")
print(f" - Saturation     : {actual_saturation}")
print(f" - Hue            : {actual_hue}")
print(f" - Gain           : {actual_gain}")
print(f" - Exposure       : {actual_exposure}")
print(f" - Autofocus      : {actual_autofocus}")




# Wait for 10 seconds
print("Waiting for 10 seconds before capturing the first image...")
time.sleep(1)

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
