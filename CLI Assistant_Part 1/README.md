# Real-Time CLI Error Assistant 🛠️

A Python-based tool that monitors your terminal in real-time, detects common CLI errors, and suggests solutions using data scraped from Stack Overflow.

![Demo](assets/demo.gif) *(Consider adding a short screen recording here)*

## ✨ Features
- **Automated Error Detection**: Uses OCR (Tesseract) to read terminal output from a specified screen region.
- **Instant Solutions**: Pulls fixes from a curated database of common CLI errors.
- **Continuous Monitoring**: Runs in background until manually stopped with `Ctrl+C`.
- **Easy Customization**: Modify error patterns/solutions via CSV file.

## 📦 Installation
1. **Clone Repository**:
   ```bash
   git clone https://github.com/yourusername/cli-error-assistant.git
   cd cli-error-assistant
* Install Dependencies

pip install -r requirements.txt

Install Tesseract OCR:

Windows: Download installer

Linux: sudo apt install tesseract-ocr

Mac: brew install tesseract


# Activate virtual environment
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Run the assistant
python cli_assistant.py


# Example Workflow:

Trigger an error in your terminal:

javac --version
The assistant detects and responds:
[RAW OCR] 'javac' is not recognized as an internal or external command...
[SOLUTION] Install JDK or add Java to PATH


🛠️ Customization
Edit Error Database:
Modify cli_errors.csv:

error_pattern,solution
"command not found","Check spelling or install package"
"Permission denied","Try running with sudo/admin privileges"


Adjust SCreen Region:

# pyautogui.screenshot(region=(x, y, width, height))
screenshot = pyautogui.screenshot(region=(100, 300, 800, 100))



# Project Structure
.
├── cli_assistant.py      # Main application logic
├── cli_errors.csv        # Error-solution database
├── scrape_so.py          # Stack Overflow scraper
├── requirements.txt      # Dependencies
└── README.md             # This documentation



🤝 Contributing
Fork the repository

Add new error patterns to cli_errors.csv

Submit a PR with clear description


## ⚠️ Known Limitations
- Requires high-contrast terminal text for best OCR accuracy
- Works best with English error messages
- Fixed screen region needs manual calibration

## 🚧 Development Status
**Note**: This project is under active development! We're continuously working to:
- Improve error detection accuracy
- Add support for more languages/error types
- Develop a user-friendly GUI interface
- Create an installable package for easy deployment

**Next Milestones**:
- [ ] Voice-based error notifications
- [ ] Auto-correct approval system
- [ ] Cross-platform deployment (Windows/Linux/Mac)

_Expect breaking changes until v1.0 release. Contributions welcome!_


📄 License
MIT License - see LICENSE for details


Happy Coding! 👨💻 If you find this useful, please ⭐ the repo!
