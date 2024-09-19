import pyautogui
import time
import pyscreeze
import cv2
import numpy as np

# Function to capture and process the screenshot
def capture_and_process_screenshot(coords):
    # Capture screenshot
    screenshot = pyautogui.screenshot(region=(coords[0], coords[1], coords[2], coords[3]))  # Adjust region as needed

    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Convert the color space from RGB to BGR (OpenCV uses BGR)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred_image, 100, 200)

    # Display the processed image
    return edges, screenshot_bgr