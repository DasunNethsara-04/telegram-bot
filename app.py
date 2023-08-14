# pip install python-telegram-bot
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from typing import Final

TOKEN: Final = ""  # your BOT token here
BOT_USERNAME: Final = ""  # your bot username here


# BOT COMMANDS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to my Testing Python BOT...")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
    The following commands are available:

    /start -> Start the BOT (Welcome Message)
    /help -> Help message
    /content -> Information about TechSARA LK content
    /contact -> Contact the Author
    """
    )


async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "You can follow our online courses for free via YouTube. Just search for TechSARA LK..."
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """You can go to my official website to contact me... Here is the link,
                                    https://techsaralk.epizy.com
                              """
    )


# RESPONSES
def handle_responses(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey there!"
    elif "how are you" in processed:
        return "I'm good!"
    elif "i love python" in processed:
        return "Remember to subscribe to my YouTube channel..."
    else:
        return "I didn't understand what you wrote."


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    response: str = ""

    print(f"User: {update.message.chat.id} in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_responses(new_text)
    else:
        response: str = handle_responses(text)

    print("BOT: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("content", content))
    app.add_handler(CommandHandler("contact", contact))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))

    # errors
    app.add_error_handler(error)

    # polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
