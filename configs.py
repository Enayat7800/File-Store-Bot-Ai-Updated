import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28150346"))
  API_HASH = os.environ.get("API_HASH", "426f0d0a1da02dea8fb71cb0bd3ab7e1")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  LUFFY_PIC = os.environ.get("LUFFY_PIC", "https://graph.org/file/1c15be412eb886ba1c8e3.jpg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Meranewbothe_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001970740972"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1251962299"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://inayatalibarkaat:enayatalibarkaat@cluster0.1gt1a4m.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002061557242")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001819528169"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""<b>╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>   
├◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├◈ Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://t.me/missqueenbotx>Fɪʟᴇ Sᴛᴏʀᴇ V𝟹</a>
╰───────────────⍟ </b> 
"""
  ABOUT_DEV_TEXT = f"""
<b>Hɪ I'M <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a>✨\n
ᴛᴀʟᴋ ᴡɪᴛʜ ᴍᴇ : <a href=https://t.me/sonali_sahaibot>Cʟɪᴄᴋ Hᴇʀᴇ</a>
ᴠɪsɪᴛ ᴍʏ ɢɪᴛʜᴜʙ : <a href=https://github.com/sonali1563>Sᴏɴᴀʟɪ's Gɪᴛʜᴜʙ</a>
ᴍʏ Cʜᴀɴɴᴇʟ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>
ᴍʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotxchat>𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥</a>
</b>
"""
  HOME_TEXT = """<b>
Hello, [{}](tg://user?id={}) 🤍\n
◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.
◈ I Cᴀɴ Gɪᴠᴇ Yᴏᴜ Dɪʀᴇᴄᴛ Aɴᴅ Bᴀᴛᴄʜ Lɪɴᴋs Jᴜsᴛ Fᴏʀᴡᴀʀᴅ Mᴇ Fɪʟᴇs.

• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @missqueenbotx
</b>"""

  Helps_data_test = """<b>
⚪️ Hᴏᴡ ᴛᴏ Usᴇ Bᴏᴛ & ɪᴛ's Bᴇɴᴇғɪᴛs?? 👇

• Sᴇɴᴅ ᴍᴇ ᴀɴʏ Fɪʟᴇ & Iᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ Mʏ Dᴀᴛᴀʙᴀsᴇ & Yᴏᴜ ᴡɪʟʟ Gᴇᴛ ᴛʜᴇ Fɪʟᴇ Lɪɴᴋ.

• Bᴇɴᴇғɪᴛs: Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ TᴇʟᴇGʀᴀᴍ Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ ᴏʀ Aɴʏ Cᴏᴘʏʀɪɢʜᴛ Cʜᴀɴɴᴇʟ, Tʜᴇɴ Iᴛs Usᴇғᴜʟ ғᴏʀ Dᴀɪʟʏ Usᴀɢᴇ, Yᴏᴜ ᴄᴀɴ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Fɪʟᴇ & I ᴡɪʟʟ Sᴇɴᴅ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴛᴏ Yᴏᴜ & Cʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ Sᴀғᴇ ғʀᴏᴍ CᴏᴘʏRɪɢʜᴛ Iɴғʀɪɴɢᴇᴍᴇɴᴛ Issᴜᴇ.

⚪️ ғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a> : <a href=https://t.me/missqueenbotxchat>Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</a>
 </b>"""
