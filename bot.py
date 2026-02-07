import logging
from telegram import Update, constants
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# --- CONFIGURATION (THE EINSTEIN SETTINGS) ---
TOKEN = 'YOUR_BOT_TOKEN_FROM_BOTFATHER'
OWNER_ID = 8550912349  # Your ID from Database 7

# --- LOGGING ---
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- SECURITY SHIELD (GOD MODE) ---
async def is_owner(update: Update):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ ERROR: Access Denied. User is not Einstein.")
        return False
    return True

# --- COMMANDS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"👑 Welcome, {user_name}. Systems are Online.\nDatabase 7 Secure.")

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kicks a user if they are a 'dumbass' (Only works for YOU)"""
    if not await is_owner(update): return
    
    if update.message.reply_to_message:
        target_id = update.message.reply_to_message.from_user.id
        await context.bot.ban_chat_member(update.message.chat_id, target_id)
        await update.message.reply_text("💥 User has been NUKED.")
    else:
        await update.message.reply_text("⚠️ Reply to a user's message to ban them.")

# --- ANTI-SPAM ENGINE ---
async def anti_spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Skip check if YOU sent it
    if update.effective_user.id == OWNER_ID: return
    
    text = update.message.text.lower() if update.message.text else ""
    
    # 1. Block Links (The Hacker Shield)
    if "http" in text or "t.me/" in text or "bit.ly" in text:
        await update.message.delete()
        await context.bot.send_message(update.message.chat_id, "🚫 SPAM DETECTED: Link Auto-Deleted.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ban", ban))
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), anti_spam))

    print("Einstein Bot is LIVE...")
    app.run_polling()
      
