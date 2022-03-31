##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "6435225"))
API_HASH = getenv('API_HASH', '4e984ea35f854762dcde906dce426c2d')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! .').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5263788485').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ''))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "lucysuppor")
LUCY_SUPPORT = getenv("LUCY_BOTS", "LUCY_BOTS")
ASS_ID = int(getenv("ASS_ID", ''))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
