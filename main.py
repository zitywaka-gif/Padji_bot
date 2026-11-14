import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo Kak! 👋 Pabji Queen Cek Resi\n"
        "Ketik resinya ya, contoh: P2611260103135\n"
        "Atau: EE123456789ID"
    )

async def cek_resi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resi = update.message.text.strip().upper()

    # Cek kalau resi kependekan
    if len(resi) < 10:
        await update.message.reply_text("Kak, resinya kayaknya kurang lengkap deh. Coba cek lagi ya 🙏")
        return

    url = f"https://www.posindonesia.co.id/id/tracking?waybill={resi}"
    await update.message.reply_text(
        f"📦 PABJI QUEEN\n"
        f"Resi: {resi}\n"
        f"Status: Sedang dicek...\n"
        f"Klik untuk cek lengkap:\n{url}\n\n"
        f"Ketik resi lain untuk cek lagi ya Kak!"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cek_resi))
    print("Bot Pabji Queen jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
