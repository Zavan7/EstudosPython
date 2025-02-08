from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p: #Objeto do Playwrigth
    '''
    p: Playwrigth 
    Objeto principal 
    Manipula Browser, Devices e Requests

    Browser:
    Vamos usar o chromium como exemplo
    Retorna e manipula contextos, em resumo, consigo manipular como o browser se comporta enquanto o código está rodando
    Exemplos: Gravar a tela / Mudara resolu;áo da tela

    Devices:
    Simila uma tela de celular, por exemplo

    Requests:
    Mas o importante é aqui, onde iremos fazer solicita
    '''
    browser = p.chromium.launch(headless=False) #Browser -> chromium
    for i in p.devices.keys():
        print(i)
    context = browser.new_context(
        color_scheme='dark',
        # record_video_dir='.',
    )
    page = context.new_page()
    page.goto('https://playwright.dev/python/')
    # sleep(5)

    print(page.text_content('#__docusaurus_skipToContent_fallback > header > div > h1 > span'))

    browser.close()