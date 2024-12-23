import cv2
import os
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Desired settings
desired_width = 2560
desired_height = 1440
desired_brightness = 128      # 0.0 to 1.0 or other range depending on driver
desired_contrast = 128      # 0.0 to 1.0 or other range
desired_saturation = 0      # 0.0 to 1.0 or other range
desired_hue = 10.0            #0 for grayscale # typical range is -180 to 180 or 0.0 to 1.0
desired_gain = 0.0            # 0.0 to ... (depends on driver)
desired_exposure = 0         # negative values often mean auto-exposure off, but this can vary
desired_autofocus = 1         # 1 for auto-focus on, 0 for off (if supported)
# ----------------------------------------------------------------------
# 1. SET all desired properties
# ----------------------------------------------------------------------
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)
#cap.set(cv2.CAP_PROP_BRIGHTNESS, desired_brightness)
#cap.set(cv2.CAP_PROP_CONTRAST, desired_contrast)
#cap.set(cv2.CAP_PROP_SATURATION, desired_saturation)
#cap.set(cv2.CAP_PROP_HUE, desired_hue)
#cap.set(cv2.CAP_PROP_GAIN, desired_gain)
#cap.set(cv2.CAP_PROP_EXPOSURE, desired_exposure)
# Some cameras do not support autofocus toggling via OpenCV, but we'll try:
#cap.set(cv2.CAP_PROP_AUTOFOCUS, desired_autofocus)

# ----------------------------------------------------------------------
# 2. READ BACK the applied properties
# ----------------------------------------------------------------------
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
actual_contrast = cap.get(cv2.CAP_PROP_CONTRAST)
actual_saturation = cap.get(cv2.CAP_PROP_SATURATION)
actual_hue = cap.get(cv2.CAP_PROP_HUE)
actual_gain = cap.get(cv2.CAP_PROP_GAIN)
actual_exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
actual_autofocus = cap.get(cv2.CAP_PROP_AUTOFOCUS)



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
