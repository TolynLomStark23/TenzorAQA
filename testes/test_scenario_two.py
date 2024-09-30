import pytest
from pages.sbis_page import SbisPage

def test_scenario_two(driver):
    sbis_page = SbisPage(driver)

    # Переход на https://sbis.ru/ в раздел "Контакты"
    sbis_page.go_to_contacts()

    # Проверка региона
    assert sbis_page.verify_region("г. Ярославль"), "Неверно определен регион"

    # Смена региона на Камчатский край
    sbis_page.change_region("Камчатский край")

    # Проверка смены региона и обновления списка партнеров
    assert sbis_page.verify_region("Камчатский край"), "Регион не изменился"
    assert "kamchatskiy-kray" in driver.current_url, "Неверный URL региона"
