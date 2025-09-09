# 📝 Singapore Attendance Checker using Selenium

## 🧠 Overview

This project is a lightweight web scraping tool designed to check student attendance from a specific online attendance portal. It uses **Selenium** and **BeautifulSoup** to extract attendance records from a dynamic webpage and compares them against a predefined list of expected students.

It demonstrates the following key capabilities:

- Automated data extraction from dynamic web pages using Selenium
- DOM parsing with BeautifulSoup
- Real-time attendance validation against an expected list
- Fully runnable via command line or Jupyter Notebook

---

## 🔑 Key Features

### ✅ Web Automation & Scraping
Uses **headless Chrome** (via Selenium) to fetch a live, JavaScript-rendered webpage.

### 📋 Attendance Validation
Compares scraped names against a full list of expected attendees and reports who has not signed in.

### 📊 Jupyter-Compatible
Easily run the script in a Jupyter notebook for quick ad hoc usage or integration with other analytics.

---

## 🗂️ Project Structure
<pre>
project-root/
│
├── src/
│ └── main.py # Attendance checking script
│
├── README.md # This file
├── requirements.txt # Python dependencies

</pre>

---

## 🖥️ How to Run the Project

### ✅ Prerequisites

- Python 3.8 or later
- Google Chrome installed
- ChromeDriver installed and available in your PATH

> 💡 *Alternatively, use `webdriver-manager` for auto-downloading the driver.*

---

### 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/attendance-checker.git
cd attendance-checker
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the script
```bash
python src/main.py
```

## 🧪 Example Output
```bash
🔄 Checking attendance...

📋 Students who have NOT signed in:
❌ SITI NAJIHAH BINTE ABU TALIB
❌ BRIAN WEE
❌ LEE JING WEI
✅ All students have signed in!
```
