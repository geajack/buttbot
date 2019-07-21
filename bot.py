from random import random

import discord

import config
import butt

class ButtBot(discord.Client):

    async def on_raw_reaction_add(self, payload):
        emoji_code = ord(payload.emoji.name)
        channel_id = payload.channel_id
        message_id = payload.message_id
        channel = await self.fetch_channel(channel_id)
        message = await channel.fetch_message(message_id)
        PEACH = 127825
        if emoji_code == PEACH:
            response, buttified = butt.buttify(message.clean_content)
            await channel.send(response)