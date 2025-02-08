from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('https://playwright.dev/python/')
    
    sleep(2)

    page.goto('https://google.com')

    sleep(2)

    page.go_back()

    sleep(2)

    page.go_forward()

    browser.close()
