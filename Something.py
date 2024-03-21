import logging
import os

import telebot

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    format='%(name)s => %(levelname)s => %(message)s'
)

main_formatter = logging.Formatter(
    "%(levelname)s => %(message)s => %(asctime)s"
)


class TelegramBotHandler(logging.Handler):
    """Handler to send telegram messages using bot"""
    def __init__(self, api_key: str, chat_id: str):
        super().__init__()
        self.api_key = api_key
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord):
        """Sends message to chat specified in .env file"""
        bot = telebot.TeleBot(self.api_key)

        bot.send_message(
            self.chat_id,
            self.format(record)
        )


class TestFilter(logging.Filter):
    """Base class to filter whether or not message should be logged """

    def filter(self, record):
        """Returns False if battle finished with a draw"""
        return not (record.msg.lower().startswith('test'))


root_logger = logging.getLogger()

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(main_formatter)

file = logging.FileHandler(filename="important_logs.txt")
file.setLevel(logging.ERROR)
file.setFormatter(main_formatter)

telegram = TelegramBotHandler(TG_BOT_TOKEN, CHAT_ID)
telegram.setLevel(logging.ERROR)
telegram.setFormatter(main_formatter)

root_logger.addHandler(console)
root_logger.addHandler(file)
root_logger.addHandler(telegram)

telegram.addFilter(TestFilter())



# MTIyMDQ1MTYxNTYyNzAyMjQxNg.GWG80x.nXVYqs3MnBKSPqKHBdG8a5gv4vuj8yi4PKqeew