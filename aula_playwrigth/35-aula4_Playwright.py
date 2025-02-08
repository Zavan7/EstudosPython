from playwright.sync_api import sync_playwright

def event (resquest_event):
    response = resquest_event.response()
    print(response.status, ' - ', resquest_event.url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on('request', event)
    page.goto('https://playwright.dev/python/')
    browser.close()