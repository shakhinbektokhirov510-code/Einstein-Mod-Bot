import logging
import random
import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. THE KEEPER (Tells Render "I'm a website, don't kill me")
app = Flask('')

@app.route('/')
def home():
    return "Einstein is Awake and Thinking!"

def run():
    # Render provides a PORT environment variable automatically
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# 2. THE BOT LOGIC
# Updated with your NEW token
TOKEN = "8344322331:AAFvWaZlHGSIva6zWYcVaLa6oTpllQ81lb8"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

QUOTES = [
    "Imagination is more important than knowledge.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "The important thing is not to stop questioning. Curiosity has its own reason for existence.",
    "Anyone who has never made a mistake has never tried anything new.",
    "Everything is relative!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Guten Tag! Einstein Bot is officially LIVE. "
        "The universe is vast, but my code is finally running! Use /quote for wisdom."
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selection = random.choice(QUOTES)
    await update.message.reply_text(f"💡 Einstein Wisdom: {selection}")

if __name__ == '__main__':
    # Start the web server in a separate thread
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
    # Start the Telegram Bot
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('quote', quote))
    
    print("Einstein Big Brain Bot is LIVE... Standing by for commands.")
    application.run_polling(drop_pending_updates=True) 
