from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('https://curso-web-scraping.pages.dev/#/exemplo/6')
driver.implicitly_wait(time_to_wait=10)

estados = driver.find_element(By.ID, 'estados')

response = estados.get_property('children')
for i in response:
    # print(i.text)
    ii = i.get_property('children')
    for y in ii:
        if y.tag_name == 'label':
            print(y.text)

        if y.tag_name == 'div':
            print('\t -', y.text)