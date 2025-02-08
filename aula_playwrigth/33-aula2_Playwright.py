from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    response = request.get('https://viacep.com.br/ws/17055180/json/')

    print(response.status)
    print(response.status_text)
    print(response.text())
    print(response.json())