from playwright.sync_api import sync_playwright
# import time
from bs4 import BeautifulSoup
import csv
from file import page_down

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

page_down(page)

print(page.content())