import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class Config:
    """Central configuration for environment variables"""

    DB_HOST=os.getenv("DB_HOST","postgres")
    DB_PORT=os.getenv("DB_PORT","5432")
    DB_USER=os.getenv("DB_USER","myuser")
    DB_PASSWORD=os.getenv("DB_PASSWORD","mypassword")
    DB_NAME=os.getenv("DB_NAME","epsilon_db")

CONFIG = Config()
