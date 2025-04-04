# Проект "Эхо-бот"

## Описание проекта

**Эхо-бот** — это простой бот, повторяющий любое сообщение, которое ему отправляют. Этот функционал часто используется для тестирования или демонстрации работы ботов. Бот может быть полезен как для новичков в разработке ботов, так и для проверки корректности взаимодействия с API.

---

## Функционал

Основной функционал **Эхо-бота** заключается в том, чтобы отвечать пользователю тем же самым сообщением, которое он отправил. 

### Пример использования:

1. Пользователь отправляет боту сообщение:  
   `"Привет, бот!"`.
2. Бот получает сообщение и обрабатывает его.
3. Бот возвращает ответ:  
   `"Привет, бот!"`.

Таким образом, бот просто копирует текст из входящего сообщения и отправляет его обратно.

---

## Техническая реализация

### Используемые технологии:

1. **Python** — язык программирования, используемый для написания логики бота.
2. **Telegram Bot API** — сервис Telegram, который позволяет создавать и управлять ботами.
3. **PythonAnywhere** — облачный хостинг, используемый для размещения кода бота и обеспечения его постоянной работы.

---

## Архитектура проекта

### 1. Настройка Telegram бота:
   - Создание бота через [@BotFather](https://t.me/BotFather).
   - Получение токена для доступа к API бота.

### 2. Реализация логики бота:
   - Использование библиотеки `python-telegram-bot` для взаимодействия с Telegram API.
   - Обработка входящих сообщений и их возврат пользователю.

### 3. Развертывание бота:
   - Код бота загружается на PythonAnywhere.
   - Настраивается автоматический запуск скрипта для постоянной работы бота.

---

## Инструкция по запуску

1. Установите необходимые зависимости:
   ```bash
   pip install python-telegram-bot
   ```

2. Замените значение переменной `TOKEN` на ваш токен бота.

3. Загрузите код на PythonAnywhere:
   - Создайте учетную запись на [PythonAnywhere](https://www.pythonanywhere.com).
   - Загрузите файл с кодом бота.
   - Настройте консоль для выполнения скрипта.

4. Запустите бота:
   - В терминале PythonAnywhere выполните команду:
     ```bash
     python your_bot_file.py
     ```
---

## Заключение

Проект **Эхо-бот** представляет собой простую, но эффективную реализацию базового функционала Telegram-бота. Он служит отличным примером для обучения и тестирования работы с API Telegram.
