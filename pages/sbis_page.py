from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"
        self.contacts_button = (By.LINK_TEXT, "Контакты")
        self.region_selector = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/div[1]')
        self.partners_list = (By.CSS_SELECTOR, "div[class*='partners']")
        self.footer_download = (By.LINK_TEXT, "Скачать локальные версии")

    def go_to_contacts(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.contacts_button)
        ).click()

    def verify_region(self, expected_region):
        region_text = self.driver.find_element(*self.region_selector).text
        return expected_region in region_text

    def change_region(self, region_name):
        self.driver.find_element(*self.region_selector).click()
        region_input = self.driver.find_element(By.ID, 'id="popup"')
        region_input.send_keys(region_name)
        self.driver.find_element(By.CSS_SELECTOR, f"span[text()='{region_name}']").click()

    def go_to_footer_download(self):
        self.driver.find_element(*self.footer_download).click()
