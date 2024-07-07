### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Это учебный проект бота для Telegram, созданный в рамках задания:

1. Напишите код для сохранения всех фото, которые отправляет пользователь боту в папке img.
2. Отправьте с помощью бота голосовое сообщение.
3. Напишите код для перевода любого текста, который пишет пользователь боту, на английский язык.

### Функциональность бота

#### 1. Сохранение фото

Бот сохраняет все фотографии, отправленные пользователями, в папке `img`. Для этого используется метод `download` из библиотеки aiogram. Когда пользователь отправляет фотографию, бот перехватывает сообщение, извлекает изображение и сохраняет его в папке `img` с использованием уникального идентификатора файла в качестве имени. Это обеспечивает уникальность каждого сохраненного изображения и предотвращает конфликты имен файлов.

#### 2. Отправка голосового сообщения

Бот отправляет голосовое сообщение, хранящееся в локальном файле. Когда пользователь отправляет команду `/voice`, бот загружает голосовое сообщение из указанного файла и отправляет его обратно пользователю. Для этого используется метод `answer_voice` и класс `FSInputFile`, который указывает путь к файлу. Это позволяет боту легко и эффективно отправлять заранее подготовленные голосовые сообщения.

#### 3. Перевод текста

Бот переводит любой текст, отправленный пользователем, на английский язык с использованием библиотеки `googletrans`. При включении режима переводчика с помощью команды `/translate_on`, бот перехватывает все текстовые сообщения, отправленные пользователем, переводит их на английский язык и отправляет перевод обратно пользователю. Для выключения режима переводчика используется команда `/translate_off`. Библиотека `googletrans` взаимодействует с API Google Translate, что позволяет боту выполнять высококачественные переводы текста в режиме реального времени.

### Установка и запуск

1. **Клонирование репозитория**:
    ```sh
    git https://github.com/NewalexOA/TG02_Aiogram_msg.git
    cd TG02_Aiogram_msg
    ```

2. **Создание виртуального окружения и установка зависимостей**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # для Linux и macOS
    .\venv\Scripts\activate  # для Windows
    pip install -r requirements.txt
    ```

3. **Создание файла конфигурации**:
    - Создайте файл `config.py` в корне проекта и добавьте в него ваш токен Telegram бота:
      ```python
      BOT_TOKEN = 'ваш_токен_бота'
      VOICE_FILE_PATH = 'path_to_voice_message.ogg'
      ```

4. **Запуск бота**:
    ```sh
    python main.py
    ```

---

## <a name="english"></a>Description in English

### Description

This is an educational project for a Telegram bot, created as part of an assignment:

1. Write code to save all photos sent by the user to the bot in the `img` folder.
2. Send a voice message using the bot.
3. Write code to translate any text sent by the user to the bot into English.

### Bot Functionality

#### 1. Saving Photos

The bot saves all photos sent by users in the `img` folder. This is achieved using the `download` method from the aiogram library. When a user sends a photo, the bot intercepts the message, extracts the image, and saves it in the `img` folder using the unique file identifier as the filename. This ensures the uniqueness of each saved image and prevents filename conflicts.

#### 2. Sending a Voice Message

The bot sends a voice message stored in a local file. When the user sends the `/voice` command, the bot loads the voice message from the specified file and sends it back to the user. This is done using the `answer_voice` method and the `FSInputFile` class, which specifies the file path. This allows the bot to easily and efficiently send pre-recorded voice messages.

#### 3. Text Translation

The bot translates any text sent by the user into English using the `googletrans` library. When the translation mode is enabled with the `/translate_on` command, the bot intercepts all text messages sent by the user, translates them into English, and sends the translation back to the user. The translation mode can be turned off using the `/translate_off` command. The `googletrans` library interacts with the Google Translate API, enabling the bot to perform high-quality text translations in real-time.

### Installation and Launch

1. **Clone the repository**:
    ```sh
    git clone https://github.com/NewalexOA/TG02_Aiogram_msg.git
    cd TG02_Aiogram_msg
    ```

2. **Create a virtual environment and install dependencies**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # for Linux and macOS
    .\venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```

3. **Create a configuration file**:
    - Create a file named `config.py` in the root directory of the project and add your Telegram bot token:
      ```python
      BOT_TOKEN = 'your_bot_token'
      VOICE_FILE_PATH = 'path_to_voice_message.ogg'
      ```

4. **Run the bot**:
    ```sh
    python main.py
    ```
