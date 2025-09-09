#📝 Singapore Attendance Checker using Selenium

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



## Project Structure

project-root/
│
├── src/
│ └── main.py # Attendance checking script
│
├── README.md # This file
├── requirements.txt # Python dependencies
