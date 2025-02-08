from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

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


# Classe de automação de login
class LoginAutomation(WebAutomation):
    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def perform_login(self, email: str, password: str):
        """Realiza o login com as credenciais fornecidas."""
        self.open_url(self.url)
        
        email_field = self.find_element(By.NAME, 'email')
        password_field = self.find_element(By.NAME, 'senha')
        submit_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()

    def clear_input(self, email_locator: tuple, password_locator: tuple):
        """Limpa o conteúdo dos campos de email e senha."""
        email_field = self.find_element(*email_locator)
        password_field = self.find_element(*password_locator)
        email_field.clear()
        password_field.clear()

# Uso do código
if __name__ == "__main__":
    URL = 'https://curso-web-scraping.pages.dev/#/exemplo/2'

    # Cria a instância e executa o processo de login
    automation = LoginAutomation(URL)
    try:
        automation.perform_login("test@teste.com", "123456")
        sleep(5)  # Espera para verificar o resultado
    except Exception as e:
        print(f"Erro: {e}")

    # Limpa os campos de email e senha
    try:
        automation.clear_input((By.NAME, 'email'), (By.NAME, 'senha'))
        sleep(5)  # Espera para verificar o resultado
    except Exception as e:
        print(f"Erro ao limpar campos: {e}")

    # Tenta realizar o login novamente
    try:
        automation.perform_login("test2@teste.com", "654321")
        sleep(5)  # Espera para verificar o resultado
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        automation.close_browser()
