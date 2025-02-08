from time import sleep
import openpyxl
from playwright.sync_api import sync_playwright

url = "https://rpachallenge.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.click('body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.instructions.col.s3.m3.l3.uiColorSecondary > div:nth-child(7) > a')
    sleep(10)
    browser.close()