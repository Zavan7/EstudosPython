from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import csv
import os

arquivo_csv = 'desafio_2.json'
arquivo_dados = 'desafio_2_dados.csv'

class WebAutomation:
    def __init__(self, url):
        self.url = url
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)
        
    def open_json(self):
        with open(arquivo_csv, 'r', encoding='utf8') as f:
            dados = json.load(f)
            return dados

    def save_csv(self, name_locator, role_locator, email_locator, phone_locator, user_locator, state_locator, image_locator):
        try:
            names = self.wait.until(EC.visibility_of_all_elements_located(name_locator))
            roles = self.wait.until(EC.visibility_of_all_elements_located(role_locator))
            emails = self.wait.until(EC.visibility_of_all_elements_located(email_locator))
            phones = self.wait.until(EC.visibility_of_all_elements_located(phone_locator))
            users = self.wait.until(EC.visibility_of_all_elements_located(user_locator))
            states = self.wait.until(EC.visibility_of_all_elements_located(state_locator))
            images = self.wait.until(EC.visibility_of_all_elements_located(image_locator))

            file_exists = os.path.isfile(arquivo_dados)

            with open(arquivo_dados, mode='a', newline='', encoding='utf8') as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(['Name', 'Role', 'Email', 'Phone', 'User', 'State', 'Image'])

                for i in range(len(names)):
                    name = names[i].text
                    role = roles[i].text
                    email = emails[i].text
                    phone = phones[i].text
                    user = users[i].text
                    state = states[i].text
                    image = images[i].get_attribute('src')

                    writer.writerow([name, role, email, phone, user, state, image])

                writer.writerow([])


            print(f"Dados salvos no arquivo {arquivo_dados} com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os dados: {e}")

    def executa(self):
        nomes = self.open_json()  
        for nome in nomes:
            print(f'Processando: {nome}')
            
            search_input_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[2]/div/div[2]/input')  
            search_button_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[2]/div/div[2]/button') 

            search_input = self.wait.until(EC.presence_of_element_located(search_input_locator))
            search_input.clear() 
            search_input.send_keys(nome)  

            search_button = self.wait.until(EC.element_to_be_clickable(search_button_locator))
            search_button.click()

            name_locator = (By.TAG_NAME, 'h3')
            role_locator = (By.TAG_NAME, 'span')
            email_locator = (By.CSS_SELECTOR, 'ul > li:nth-child(1)')
            phone_locator = (By.CSS_SELECTOR, 'ul > li:nth-child(2)')
            user_locator = (By.CSS_SELECTOR, 'ul > li:nth-child(3)')
            state_locator = (By.CSS_SELECTOR, 'ul > li:nth-child(4)')
            image_locator = (By.TAG_NAME, 'img')

            self.save_csv(name_locator, role_locator, email_locator, phone_locator, user_locator, state_locator, image_locator)


# Execução
if __name__ == '__main__':
    automacao = WebAutomation('https://curso-web-scraping.pages.dev/#/desafio/2')
    automacao.executa()
