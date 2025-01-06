import cv2
import requests
import os

def capture_and_upload_image(api_url, farm_token):
    """
    Captures an image from the webcam, saves it as a temporary JPEG file,
    and uploads it to the provided API URL.

    Parameters:
        api_url (str): The URL to which the image and farm_token should be sent.
        farm_token (str): The farm token to include in the POST request.

    Returns:
        dict: A dictionary containing the response status and data.
    """
    # Initialize the camera (0 is the default camera index)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return {"status": "error", "message": "Could not open camera."}

    # Capture a frame
    ret, frame = camera.read()

    # Release the camera after capturing
    camera.release()

    if not ret:
        return {"status": "error", "message": "Could not read frame from camera."}

    # Save the frame as a temporary file
    temp_filename = "temp.jpg"
    try:
        cv2.imwrite(temp_filename, frame)

        # Prepare the POST request payload
        files = {
            'image': (temp_filename, open(temp_filename, 'rb'), 'image/jpeg')
        }
        data = {
            'farm_token': farm_token
        }

        # Send the POST request
        response = requests.post(api_url, files=files, data=data)

        # Return the response from the server
        return {
            "status": "success" if response.status_code == 200 else "error",
            "message": response.text,
            "status_code": response.status_code,
            "temp_file": temp_filename
        }
    except Exception as e:
        return {"status": "error", "message": str(e), "temp_file": temp_filename}

# Example usage
if __name__ == "__main__":
    api_url = "https://smartseaweed.site/Real/upload_img.php"
    farm_token = "95cae43727abd5ac940d28f713af5621"

    result = capture_and_upload_image(api_url, farm_token)
    print(result)
    print(f"Temporary file saved as: {result['temp_file']}")
