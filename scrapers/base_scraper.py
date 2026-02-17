from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseScraper:
    def __init__(self, headless=False):
        self.options = Options()
        if headless: self.options.add_argument("--headless")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        self.driver = None

    def iniciar_driver(self):
        if not self.driver:
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def cerrar_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def obtener_texto_elemento(self, url, selector_tipo, selector_valor, timeout=10):
        self.iniciar_driver()
        self.driver.get(url)
        time.sleep(3)
        elemento = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((selector_tipo, selector_valor))
        )
        return elemento.text.strip()