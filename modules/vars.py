# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "27665762")
API_HASH  = os.environ.get("API_HASH", "b2b6f18e1280f194b8f7349db4737eb9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6746702961:AAHpksRXgLYM3A5zboILn0me-uUtVg813oU") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

