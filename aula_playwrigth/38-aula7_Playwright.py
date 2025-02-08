from time import sleep
from playwright.sync_api import sync_playwright

url = "https://playwright.dev/python/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.locator('#__docusaurus > nav > div.navbar__inner > div:nth-child(1) > a:nth-child(3)').click()
    pr = page.locator('#__docusaurus_skipToContent_fallback > div > div > main > div > div > div.col.docItemCol_VOVn > div > article > div.theme-doc-markdown.markdown > p:nth-child(3)')
    print(pr.text_content())
    sleep(5)
    browser.close()