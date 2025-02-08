import pyautogui
import pytesseract
import pandas as pd
import time
import re

# Load error database
error_db = pd.read_csv("cli_errors.csv")

def monitor_terminal():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path if needed
    while True:
        # Capture only the latest terminal line (adjust coordinates!)
        screenshot = pyautogui.screenshot(region=(0,0, 800, 600))
        text = pytesseract.image_to_string(screenshot)
        text = text.strip()
        text = re.sub(r'\n+', ' ', text)
        print(f"Raw OCR text: {text}")  # Debugging
        
        # Check for errors
        if text:
            for index, row in error_db.iterrows():
                try:
                    re.compile(row['error_pattern'])  # Validate regex syntax
                    if re.search(row['error_pattern'], text, re.IGNORECASE):
                        print(f"Match: {row['error_pattern']}")
                except re.error as e:
                    print(f"BAD REGEX in row {index}: '{row['error_pattern']}'")
                    print(f"Error: {e}\n")
                    break  # Stop on first error
        time.sleep(2)

if __name__ == "__main__":
    monitor_terminal()