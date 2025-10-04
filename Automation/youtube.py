# youtube.py
import re, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_video_query(command):
    pattern = r"(?:play|search for)\s+(.*?)\s*(?:on youtube|youtube)?$"
    match = re.search(pattern, command.lower())
    return match.group(1).strip() if match else command.strip()

def play_youtube_video(query):
    print(f"🔍 Searching YouTube for: {query}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('a', href=True):
        if "/watch?v=" in link['href']:
            video_url = "https://www.youtube.com" + link['href']
            break
    else:
        print("❌ No video found.")
        return

    print("▶️ Playing:", video_url)
    driver.get(video_url)

