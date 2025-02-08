import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Configure
TAG = "command-line"  # Stack Overflow tag (e.g., "pip", "bash", "linux")
PAGES = 20
CSV_FILE = "cli_errors.csv"

# Create DataFrame to store errors and solutions
df = pd.DataFrame(columns=["error_pattern", "solution"])

for page in range(1, PAGES + 1):
    url = f"https://stackoverflow.com/questions/tagged/{TAG}?tab=votes&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract questions and answers
        questions = soup.select("#questions .js-post-summary")
        for q in questions:
            title = q.select_one(".s-post-summary--content-title").get_text(strip=True)
            answer = q.select_one(".s-post-summary--content-excerpt").get_text(strip=True)
            
            # Clean and generalize errors (example: replace specific file paths)
            error_pattern = re.sub(r"file '.*?'", "file '.*'", title)
            solution = answer.split("Answer:")[-1].strip() if "Answer:" in answer else answer
            
            df = pd.concat([df, pd.DataFrame([{"error_pattern": error_pattern, "solution": solution}])], ignore_index=True)
        
        print(f"Page {page} scraped. Total entries: {len(df)}")
    
    except Exception as e:
        print(f"Failed to scrape page {page}: {e}")

# Save to CSV
df.to_csv(CSV_FILE, index=False)
print(f"Saved {len(df)} entries to {CSV_FILE}")