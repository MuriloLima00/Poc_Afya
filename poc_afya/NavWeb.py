from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import AntiCaptcha

def navOptions(path_pasta):
    options = Options()
    options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    options.set_preference('security.tls.version.min', 1)
    options.set_preference('browser.download.dir',path_pasta.replace('/','\\'))
    options.set_preference('browser.download.folderList', 2)
    #options.add_argument('--headless')
    navegador = webdriver.Firefox(executable_path='C:/Users/murilo.lima/Desktop/Guardar/Webdrivers/Mozilla_driver/geckodriver.exe', options=options)

    return navegador

def navWeb(pasta, user, senha):
    navegador = navOptions(pasta)

    navegador.maximize_window()
    navegador.get('http://sisfies.mec.gov.br/')
    
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[2]/td[2]').click()
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/table[2]/tbody/tr/td[2]/div/div[2]/center/table/tbody/tr/td[2]/a/table/tbody/tr[2]/td[2]').click()

    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="id"]').send_keys(user)
    sleep(.5)
    navegador.find_element(By.XPATH, '//*[@id="pw"]').send_keys(senha)
    sleep(.5)
    navegador.find_element(By.XPATH, '//*[@id="botoes"][@value="Autenticar"]').click()

    sleep(1)
    try:
        selectPerfil = navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[1]/ul/li[4]/form/select')
        cb = Select(selectPerfil)
        cb.select_by_value('141')
    except NoSuchElementException:
        pass

    sleep(.5)
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[3]/ul/li[2]/a').click()

    url = navegador.current_url
    captcha = navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/form/div[6]/span/div').get_attribute('data-sitekey')

    resp = AntiCaptcha.captchaSolver(url, captcha)
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resp}'")

    sleep(.5)
    navegador.find_element(By.XPATH, '//*[@id="excel"]').click()

    sleep(10)
    navegador.close()