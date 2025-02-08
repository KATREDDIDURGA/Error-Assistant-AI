import pyautogui
import pytesseract
from PIL import Image

# Capture a region of the screen (adjust coordinates for your terminal window)
screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # (x, y, width, height)
screenshot.save("terminal_screenshot.png")

# Extract text using OCR
text = pytesseract.image_to_string(screenshot)
print("Extracted Text:\n", text)