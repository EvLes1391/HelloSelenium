# Проект: Автоматизация тестирования с Selenium

![Python](https://img.shields.io/badge/Python-3.13.2%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.31.0-red)
![Pytest](https://img.shields.io/badge/Pytest-8.3.5-green)

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
│   ├── __init__.py       # Для создания Python-пакета
│   ├── base_page.py      # Фундамент РОМ
│   └── google_page.py    # Инкапсуляция взаимодействия с Google
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
