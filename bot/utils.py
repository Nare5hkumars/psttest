from pyrogram import Client
import os

def download_link(client:Client,message,file_id):
  file=client.download_media(file_id)
  if file:
    message.reply_photo(file)
    os.remove(file)
  else:
    message.reply_text("Failed to Download")
