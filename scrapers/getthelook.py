from scrapers.base_scraper import BaseScraper
from selenium.webdriver.common.by import By

class GetTheLookScraper(BaseScraper): # Cambiá el nombre de la clase según el archivo
    def obtener_precio(self, url):
        # Este selector es más genérico y suele sobrevivir a los cambios de página
        selector_vtex = ".vtex-product-price-1-x-sellingPriceValue, .vtex-product-price-1-x-price"
        return self.obtener_texto_elemento(url, By.CSS_SELECTOR, selector_vtex)