import os

from dotenv import load_dotenv

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv('../.env')



BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
WEBAPP_URL = os.getenv("WEBAPP_URL")
IMGBB_API_KEY = os.getenv('IMGBB_API_KEY')

if not BOT_TOKEN:

    raise ValueError("BOT_TOKEN not found in .env")

if not ADMIN_ID:

    raise ValueError("ADMIN_ID not found in .env")

if not WEBAPP_URL:

    raise ValueError("WEBAPP_URL not found in .env")


if not IMGBB_API_KEY:

    raise ValueError("IMGBB_API_KEY not found in .env")
