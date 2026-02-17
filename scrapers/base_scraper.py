from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class BaseScraper:
    def __init__(self, headless=True):
        self.driver = None
        self.options = Options()
        
        # Kit de supervivencia para GitHub Actions
        if headless:
            self.options.add_argument("--headless=new") # La versión 'new' es más estable
        
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    def iniciar_driver(self):
        if not self.driver:
            # Esto instala el driver automáticamente en el servidor
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=self.options)
            
            # Ocultar que es un bot
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def cerrar_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def obtener_texto_elemento(self, url, selector_type, selector_value):
        try:
            self.iniciar_driver()
            self.driver.get(url)
            time.sleep(5) # Un poco más de tiempo por las dudas
            elemento = self.driver.find_element(selector_type, selector_value)
            return elemento.text
        except Exception as e:
            print(f"Error en el scraping: {e}")
            return None
        finally:
            self.cerrar_driver()