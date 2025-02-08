from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep, time


class WebAutomation:
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)

    def get_element(self, locator):
        return self.wait.until(EC.title_contains(locator))

    def executa(self):
        start_time = time()
        self.driver.get(self.url)
        text = self.get_element('mador')
        end_time = time()
        elapsed_time = end_time - start_time 
        print(f"Texto encontrado: {text}")
        print(f"Tempo de execução: {elapsed_time:.2f} segundos")


if __name__ == '__main__':
    automacao = WebAutomation('https://curso-web-scraping.pages.dev/#/exemplo/5')
    automacao.executa()
