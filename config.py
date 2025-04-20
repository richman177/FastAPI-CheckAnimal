import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGODB_URL = os.getenv('MONGODB_URL')
    DB_NAME = os.getenv('DB_NAME')
    ROBOFLOW_URL = os.getenv('ROBOFLOW_URL')


config = Config()
