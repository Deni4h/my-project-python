from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Dictionary respons chatbot
response = {
    'hi': 'Hi! Ada yang bisa saya bantu?',
    'apa kabar': 'Saya baik, bagaimana denganmu?',
    'terima kasih': 'Sama-sama! 😊'
}

# Fungsi untuk menangani pesan dari user
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    reply = response.get(text, "Maaf, saya tidak mengerti.")  
    await update.message.reply_text(reply)

# Fungsi untuk perintah /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Saya chatbot Telegram. Coba ketik 'hi' atau 'apa kabar'.")

# Fungsi utama untuk menjalankan bot
def main():
    TOKEN = "7922086771:AAFFiPHoIA8lowhDnT8ajP6HL-8JDou__Sc"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

# Jalankan bot
if __name__ == "__main__":
    main()
