from pyrogram import Client,filters
from bot.database import save_post,get_last_post
from bot.utils import download_media
from config import API_ID,API_HASH,BOT_TOKEN

app=Client("media_post_bot",API_ID,API_HASH,BOT_TOKEN)
def start(client,message):
  message.reply_text("Hello! send me")

def save_text(client,message):
  save_post(message.from_user.id,text=message.text)
  message.reply_text("Your text has been saved")

def last_post(client,message):
  post=get_last_post(message.from_user.id)
  if post:
    if post.get("text"):
      message.reply_text(f"Last post (text):\n\n{post['text']}")
    elif post.get("file_id"):
      download_media(client,message,post[file_id])
    else:
      message.reply_text("No post found")
  else:
    message.reply_text("No post found")
