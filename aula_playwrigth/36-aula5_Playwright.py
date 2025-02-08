from playwright.sync_api import sync_playwright

url = "https://playwright.dev/python/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    h1 = page.locator('#__docusaurus_skipToContent_fallback > header > div > h1')
    print (h1.text_content())
    browser.close()