# Проект: Автоматизация тестирования с Selenium

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0-red)
![Pytest](https://img.shields.io/badge/Pytest-7.0-green)

Проект демонстрирует базовые возможности Selenium WebDriver с использованием:
- Автоматической загрузки драйверов через WebDriverManager
- Ожиданий WebDriverWait
- Тестовой структуры pytest

## 📁 Структура проекта
```
HelloSelenium/
├── tests/
│   └── test_google.py    # Тесты поиска Google
├── pages/                # Для будущих Page Objects
├── .gitignore
├── requirements.txt      # Зависимости
└── README.md             (этот файл)
```

## 🛠 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/EvLes1391/HelloSelenium.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Запуск тестов
```bash
pytest tests/ -v
```

## 📝 Пример теста
```python
def test_google_search():
    driver.get("https://google.com")
    assert "Google" in driver.title