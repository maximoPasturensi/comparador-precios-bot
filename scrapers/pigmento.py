from scrapers.base_scraper import BaseScraper
from selenium.webdriver.common.by import By

class PigmentoScraper(BaseScraper):
    def obtener_precio(self, url):
        # En tu captura se ve que es VTEX igual que Farmacity!
        # Vamos a usar el selector exacto que resalta en azul tu inspector
        selector = ".vtex-product-price-1-x-sellingPriceValue"
        
        # Usamos el método de la madre que ya tiene el WebDriverWait
        precio = self.obtener_texto_elemento(url, By.CSS_SELECTOR, selector)
        
        if precio:
            return precio
        
        # Si el anterior falla, buscamos este otro que también se ve en tu foto
        return self.obtener_texto_elemento(url, By.CLASS_NAME, "vtex-product-price-1-x-currencyContainer")