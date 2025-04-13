from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

TOKEN_FILE = 'tokens.json'
BOT_TOKEN = '7885680963:AAH--Wh2ubwwcgElTTyEI7IdXF_VLw9uBkE'

def load_tokens():
    try:
        with open(TOKEN_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_tokens(tokens):
    with open(TOKEN_FILE, 'w') as f:
        json.dump(tokens, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用 Mint 地址机器人！\n使用 /addmint <地址> 添加新 token")

async def add_mint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("请使用格式：/addmint <mint地址>")
        return
    new_mint = context.args[0]
    tokens = load_tokens()
    if new_mint in tokens:
        await update.message.reply_text("这个 mint 已经在列表里了。")
    else:
        tokens.append(new_mint)
        save_tokens(tokens)
        await update.message.reply_text(f"添加成功！当前总数：{len(tokens)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("addmint", add_mint))

app.run_polling()
