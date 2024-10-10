import os
import logging
from dotenv import load_dotenv # type: ignore

load_dotenv(os.path.join(os.path.dirname(__file__), '../config/.env'))

class Logger:
    @staticmethod
    def setup_logger():
        logging.basicConfig(filename='logs/bot.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    @staticmethod
    def read_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        return None

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
