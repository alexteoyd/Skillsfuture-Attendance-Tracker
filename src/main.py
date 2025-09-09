from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# ====== YOUR FULL EXPECTED STUDENT LIST ======
expected_students = [
    "MOHAMMAD FAHMY BIN MAHAMUD",
    "NURUL KHAIRIAH BINTE ABDUL KADIR",
    "RAKHI THULASIDEVI",
    "SITI NAJIHAH BINTE ABU TALIB",
    "LUO QIUFENG",
    "YONG SHET MING",
    "PASHA SIRAJ",
    "WONG YUE XIN",
    "KEH SIOK YAN",
    "KONG YUYUN",
    "GOWRY CHANDRA SEGARAN",
    "CHOW KWONG MENG",
    "MASHURE RAHMAN",
    "LIM FENG RUI EDMUND",
    "BRIAN WEE",
    "HO CHOO GEOK",
    "CHAN YUAN HUI",
    "MIKE TAN YONG EN",
    "NUR ADRIANA BINTE MOHAMED YAZID",
    "LEE JING WEI",
    "GOH CHONG HENG",
    "AZFAR BIN AZMI",
    "MADHUSUDHAN SWATHI",
    "ALEX TEO",
    "YUEN VEESHEEN",
    "TESTER 1"  # If needed
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
