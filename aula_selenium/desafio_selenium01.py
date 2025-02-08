from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from time import sleep
import calendar
import datetime
import json

# Caminho para o arquivo de dados
dados = Path(__file__).parent / 'desafio_1.json'
url = 'https://curso-web-scraping.pages.dev/#/desafio/1'

# Carrega os dados do arquivo JSON
with open(dados, 'r') as f:
    data = json.load(f)

class WebAutomation:
    def __init__(self):
        # Usa o webdriver-manager para configurar o WebDriver automaticamente
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_url(self, url: str):
        """Abre o site no navegador."""
        self.driver.get(url)

    def find_element(self, by: By, value: str):
        """Localiza um elemento na página."""
        return self.driver.find_element(by, value)

    def close_browser(self):
        """Fecha o navegador."""
        self.driver.quit()

    def preencher_formulario(self, dados):
        """Preenche o formulário com os dados fornecidos."""
        for dado in dados:
            # Preenchendo o campo de e-mail
            email = self.find_element(By.NAME, 'email')
            email.send_keys(dado['email'])

            # Preenchendo o campo de senha
            senha = self.find_element(By.NAME, 'senha')
            senha.send_keys(dado['senha'])

            # Preenchendo o campo de dia de nascimento
            dia = Select(self.find_element(By.NAME, 'dia'))
            dia.select_by_visible_text(dado['data-de-nascimento'].split('-')[2].lstrip('0'))

            # Preenchendo o campo de mês de nascimento
            mes = Select(self.find_element(By.NAME, 'mes'))
            mes.select_by_index(int(dado['data-de-nascimento'].split('-')[1]) - 1)
            mes_nome = mes.first_selected_option.text

            # Preenchendo o campo de ano de nascimento
            ano = Select(self.find_element(By.NAME, 'ano'))
            ano.select_by_visible_text(dado['data-de-nascimento'].split('-')[0])

            # Marcando ou desmarcando a opção de newsletter
            newsletter = self.find_element(By.ID, 'airplane-mode')
            if dado['newsletter']:
                newsletter.click()

            # Clicando no botão de envio
            submit_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            submit_button.click()

            self.clear_input('email', 'senha')

    def clear_input(self, email, senha):
        """Limpa o conteúdo dos campos de email e senha."""
        self.email_field = self.find_element(By.NAME, email)
        self.password_field = self.find_element(By.NAME, senha)
        self.email_field.clear()
        self.password_field.clear()

    def executar(self):
        """Executa o processo de automação."""
        self.open_url(url)
        self.preencher_formulario(data)
        self.clear_input('email', 'senha')
        sleep(5)  # Aguarde 5 segundos antes de fechar
        self.close_browser()

if __name__ == "__main__":
    automacao = WebAutomation()
    automacao.executar()
