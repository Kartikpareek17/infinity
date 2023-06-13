from telethon import TelegramClient
import logging
import time 


#openai_key = "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"
api_id = "20307178"
api_hash = "f047c24a556d09b3a652b27715b86ba3"
#bot_token = "6023828892:AAFEGAJnCVTIzbgrA_WZOHRHekgha6wCDL8"
bot_token = "5976807380:AAH2RhzbT_qwyubcO6Y-yAx_hdo9zzpYb4I"

bot = TelegramClient("kbot", api_id, api_hash).start(bot_token=bot_token)