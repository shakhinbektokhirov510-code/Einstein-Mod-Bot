import logging
import random
import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 1. THE FAKE WEBSITE (To keep Render happy)
app = Flask('')
@app.route('/')
def home():
    return "Einstein is Awake!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# 2. THE BOT LOGIC
TOKEN = "8344322331:AAFvWaZlHGSIva6zWYcVaLa6oTpllQ81lb8"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

QUOTES = [
    "Imagination is more important than knowledge.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "The important thing is not to stop questioning.",
    "Anyone who has never made a mistake has never tried anything new."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Guten Tag! Einstein Bot is officially LIVE from Philly. Use /quote!")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💡 Einstein Wisdom: {random.choice(QUOTES)}")

if __name__ == '__main__':
    # Start the fake website in the background
    t = Thread(target=run)
    t.start()
    
    # Start the Telegram Bot
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('quote', quote))
    
    print("Einstein Big Brain Bot is LIVE...")
    application.run_polling()
    
