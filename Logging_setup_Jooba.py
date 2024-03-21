import logging
import os
import sys
import discord 
import requests


logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    format='%(name)s => %(levelname)s => %(message)s'
)

main_formatter = logging.Formatter(
    "%(name)s *>> %(levelname)s *>> %(message)s *>> %(asctime)s *>> %(filename)s",
    datefmt='%Y/%m/%d %H:%M:%S'
)

class DiscordHandler(logging.Handler):
    def __init__(self, webhook_url: str):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        requests.post(self.webhook_url, json={"content": self.format(record), "username": "JoobaBot"})


class TestFilter(logging.Filter):
    """Base class to filter whether or not message should be logged """
    def filter(self, record):
        return not (record.msg.lower().startswith('jooba'))


root_logger = logging.getLogger()

discord1 = DiscordHandler("https://discord.com/api/webhooks/1220492366365069322/5N8_KJj231hfz6eVXx75w3siZe6ONaofU8qrX76y_x_nb0mu4HK8vstjwZ67iIaWfvEC")

discord1.setLevel(logging.DEBUG)
discord1.setFormatter(main_formatter)

root_logger.addHandler(discord1)

root_logger.critical("Vaime, WOW!")

root_logger.addFilter(TestFilter())

root_logger.critical("Who is Very cool!")
root_logger.critical("Jooba is Very cool!")

for i in range(0, 20):
    root_logger.warning(f"SomeOne is sending warning number {i}")

