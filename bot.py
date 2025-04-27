from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Tokeninizi burada qeyd edin
TOKEN = '7685506993:AAFdBHjVyvHNDTy08i2bZDcKM4gyEjyCEmc'

# Komanda funksiyası
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salam, botunuz işə düşdü!')

def main():
    # Application obyekti yaradın
    application = Application.builder().token(TOKEN).build()

    # Komanda handler əlavə edin
    application.add_handler(CommandHandler('start', start))

    # Botu işə salın
    application.run_polling()

if __name__ == '__main__':
    main()
