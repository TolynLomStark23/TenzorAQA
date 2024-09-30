from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.banner = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
        self.sila_v_lyudyah = (By.NAME, "Сила в людях")
        self.details_link = (By.LINK_TEXT, "Подробнее")
        self.timeline_photos = (By.CSS_SELECTOR, "img[class*='timeline-photo']")

    def click_tensor_banner(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.banner)
        ).click()

    def verify_sila_v_lyudyah_exists(self):
        WebDriverWait(self.driver, 10)
        return self.driver.find_element(*self.sila_v_lyudyah)

    def go_to_about_page(self):
        self.driver.find_element(*self.details_link).click()

    def verify_photo_sizes(self):
        photos = self.driver.find_elements(*self.timeline_photos)
        sizes = [(photo.size['height'], photo.size['width']) for photo in photos]
        return all(size == sizes[0] for size in sizes)  # Проверяем, что все размеры одинаковые
