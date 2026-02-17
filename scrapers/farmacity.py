from scrapers.base_scraper import BaseScraper
from selenium.webdriver.common.by import By

class FarmacityScraper(BaseScraper):
    def obtener_precio(self, url):
        # Selector estándar de Vtex para precio
        return self.obtener_texto_elemento(url, By.CLASS_NAME, "vtex-product-price-1-x-sellingPriceValue")


