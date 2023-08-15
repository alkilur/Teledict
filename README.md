# telebot

Just a trainy telegram bot project.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [SQLite](https://www.sqlite.org/)
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```

2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install pyTelegramBotAPI
   ```
   
3. Create your telegram bot and get token, using @BotFather:
   ```bash
   # main.py
   bot = telebot.TeleBot('<token_from_BotFather>')
   ```

4. Create a database and insert content into it using "db_create.py"
   Run the project with the main.py file
