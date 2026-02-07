import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Your Token
TOKEN = "8344322331:AAFvWaZlHGSIva6zWYcVaLa6oTpllQ81lb8"

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- THE BIG BRAIN QUOTES ---
QUOTES = [
    "Imagination is more important than knowledge.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "The important thing is not to stop questioning. Curiosity has its own reason for existence.",
    "Anyone who has never made a mistake has never tried anything new.",
    "Try not to become a man of success, but rather try to become a man of value."
]

# --- COMMANDS ---

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Guten Tag, {user_name}! I am the Einstein Bot.\n\n"
        "I am currently running on a server in Ohio, powered by a legend in Philadelphia. "
        "Use /quote to hear my wisdom, or just talk to me!"
    )

# /quote command
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selection = random.choice(QUOTES)
    await update.message.reply_text(f"💡 Einstein Wisdom: {selection}")

# Respond to normal messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "hello" in text or "hi" in text:
        await update.message.reply_text("Hello! My brain is currently calculating the universe... and your next question.")
    elif "philly" in text:
        await update.message.reply_text("Philadelphia? A city of great energy and even greater cheesesteaks!")
    else:
        await update.message.reply_text("Interesting point. As I always say, everything is relative!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('quote', quote))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Einstein Big Brain Bot is LIVE...")
    application.run_polling()
    
