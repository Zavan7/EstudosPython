from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

url = 'https://curso-web-scraping.pages.dev/#/exemplo/4'

# Usa o webdriver-manager para configurar o WebDriver automaticamente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
wait = WebDriverWait(driver, 10)
vantagens = wait.until(EC.presence_of_element_located(locator=(By.ID, 'vantagens')))
print(vantagens.text)
sleep(3)
driver.quit()