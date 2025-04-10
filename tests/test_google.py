import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from pages import GooglePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture
def google_page(browser: WebDriver):
    page = GooglePage(browser)
    browser.get("https://www.google.com")
    return page

SEARCH_QUERIES = [
    ('Hello Selenium', 'Selenium'),
    ('QA', 'тестировщик'),
    ('Доллар за 100к', 'курс доллара'),
]

@pytest.mark.parametrize("query, expected_text", SEARCH_QUERIES)
def test_google_search(google_page: GooglePage, query: str, expected_text: str):
    # Проверка заголовка
    assert "Google" in google_page.get_title(), "Неверный заголовок"

    # Поиск и проверка результатов
    google_page.search(query)
    first_result = google_page.get_first_result_text()
    assert query in first_result, f"Запрос '{query}' не найден в первом результате"
    assert expected_text in first_result, (
        f"Ожидаемый текст '{expected_text}' не найден в результате"
    )

    # Тест 3: Проверка 3-го результата
    third_result = google_page.get_nth_result_text(3)
    assert third_result, "No найдено 3 результата поиска"
