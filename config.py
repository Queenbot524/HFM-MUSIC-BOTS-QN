from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/db62e20be4e685a5d0716.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/a749f8c1d606437a8b579.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EBD_QN_CHAT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EBD_QN")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1476655690").split()))


FAILED = "https://telegra.ph/file/c9bf09ab92ce5432b4cb7.jpg"
