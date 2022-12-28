#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode, ChatType
import sys
from datetime import datetime

from config import (
    API_HASH, 
    APP_ID, 
    LOGGER,
    TG_BOT_TOKEN, 
    TG_BOT_WORKERS, 
    FORCE_SUB_1,  
    FORCE_SUB_2,  
    FORCE_SUB_3,  
    FORCE_SUB_4,  
    CHANNEL_ID, 
    PORT
)


name_s ="""
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
"""

name_s = """
        ____  ___ _    ______
       / __ \/   | |  / /  _/
      / / / / /| | | / // /  
     / /_/ / ___ | |/ // /   
    /_____/_/  |_|___/___/   
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.username = usr_bot_me.username
        self.namebot = usr_bot_me.first_name
        self.uptime = datetime.now()
        print(f"BOT BERHASIL DIDETEKSI\nFirst Name: {self.namebot}\nUsername: @{self.username}\n")

        if FORCE_SUB_1:
            try:
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                self.type1 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = (await self.get_chat(FORCE_SUB_1)).invite_link
                self.invitelink1 = link
                print(f"FORCE SUB 1 DI DETEKSI\nTitle: {info.title}\nChatID: {info.id}\n")
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_1!")
                self.LOGGER(__name__).warning(f"Silahkan periksa kembali nilai FORCE_SUB_1 dan Pastikan bot @{self.username} adalah admin dichannel dengan mengundang pengguna melalui Izin tautan, Nilai Sub Saluran Saat ini : {FORCE_SUB_1}")
                sys.exit()
        if FORCE_SUB_2:
            try:
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                self.type2 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = (await self.get_chat(FORCE_SUB_2)).invite_link
                self.invitelink2 = link
                print(f"FORCE SUB 2 DI DETEKSI\nTitle: {info.title}\nChatID: {info.id}\n")
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_2!")
                self.LOGGER(__name__).warning(f"Silahkan periksa kembali nilai FORCE_SUB_2 dan Pastikan bot @{self.username} adalah admin dichannel dengan mengundang pengguna melalui Izin tautan, Nilai Sub Saluran Saat ini : {FORCE_SUB_2}")
                sys.exit()
        if FORCE_SUB_3:
            try:
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                self.type3 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_3)
                    link = (await self.get_chat(FORCE_SUB_3)).invite_link
                self.invitelink3 = link
                print(f"FORCE SUB 3 DI DETEKSI\nTitle: {info.title}\nChatID: {info.id}\n")
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_3!")
                self.LOGGER(__name__).warning(f"Silahkan periksa kembali nilai FORCE_SUB_3 dan Pastikan bot @{self.username} adalah admin dichannel dengan mengundang pengguna melalui Izin tautan, Nilai Sub Saluran Saat ini : {FORCE_SUB_3}")
                sys.exit()
        if FORCE_SUB_4:
            try:
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                self.type4 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = (await self.get_chat(FORCE_SUB_4)).invite_link
                self.invitelink4 = link
                print(f"FORCE SUB 4 DI DETEKSI\nTitle: {info.title}\nChatID: {info.id}\n")
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_4!")
                self.LOGGER(__name__).warning(f"Silahkan periksa kembali nilai FORCE_SUB_4 dan Pastikan bot @{self.username} adalah admin dichannel dengan mengundang pengguna melalui Izin tautan, Nilai Sub Saluran Saat ini : {FORCE_SUB_4}")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
            print(f"CHANNEL DATABASE DI DETEKSI\nTitle: {info.title}\nChatID: {info.id}\n")
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin dichannel Database anda, ChannelID saat ini: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by Dvajr")
        print(f"""{name_s}""")
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
