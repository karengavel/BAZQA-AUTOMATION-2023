from selenium.common import NoSuchElementException


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    # Metodo que indica si un elemento es mostrado en pantalla
    def elemento_es_mostrado(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False
