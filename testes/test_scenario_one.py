import pytest
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage

def test_scenario_one(driver):
    sbis_page = SbisPage(driver)
    tensor_page = TensorPage(driver)

    # Переход на https://sbis.ru/ в раздел "Контакты"
    sbis_page.go_to_contacts()

    # Найти баннер Тензор и кликнуть по нему
    tensor_page.click_tensor_banner()

    # Переход на https://tensor.ru/ и проверка блока "Сила в людях"
    assert tensor_page.verify_sila_v_lyudyah_exists(), "Блок 'Сила в людях' не найден"

    # Переход в "Подробнее" и проверка открытия страницы https://tensor.ru/about
    tensor_page.go_to_about_page()
    assert "about" in driver.current_url, "Неправильный URL страницы"

    # Проверка одинаковых размеров фотографий
    assert tensor_page.verify_photo_sizes(), "Фотографии имеют разные размеры"
