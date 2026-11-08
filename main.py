import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = os.getenv("TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Kak! 👋 Pabji Queen Cek Resi\nKetik resinya ya, contoh: P2611260103135")
async def cek_resi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resi = update.message.text.strip().upper()
    url = f"https://www.posindonesia.co.id/id/tracking?waybill={resi}"
    await update.message.reply_text(f"📦 PABJI QUEEN\nResi: {resi}\nKlik untuk cek:\n{url}")
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cek_resi))
app.run_polling()
