from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# ====== YOUR FULL EXPECTED STUDENT LIST ======
expected_students = [
    "ALEX TEO",
    "STUDENT 1",
    "STUDENT 2" # If needed
]

# ====== URL TO CHECK ======
ATTENDANCE_URL = "https://www.myskillsfuture.gov.sg/api/take-attendance/RA576194"

def fetch_signed_names():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Start browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(ATTENDANCE_URL)

    # Wait for JS to populate the page (can adjust if slow connection)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    signed_names = []

    attendance_info = soup.find("div", class_="row attendance-info")
    if not attendance_info:
        print("❌ Could not find attendance-info block. Page might not have loaded correctly.")
        return signed_names

    attendance_items = attendance_info.find_all("div", class_="attendance-item")
    for item in attendance_items:
        name_tag = item.find("span", class_="attendance-name")
        if name_tag:
            signed_names.append(name_tag.text.strip().upper())

    return signed_names

# Directly call your logic in Jupyter
print("🔄 Checking attendance...")
signed_names = fetch_signed_names()

if not signed_names:
    print("⚠️ No signed-in names found. Check if the URL is correct or requires login.")
else:
    missing = [name for name in expected_students if name.upper() not in signed_names]

    print("\n📋 Students who have NOT signed in:")
    if missing:
        for name in missing:
            print(f"❌ {name}")
    else:
        print("✅ All students have signed in!")
