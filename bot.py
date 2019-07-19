from random import random

import discord

import config
import butt

class ButtBot(discord.Client):

    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        emoji_code = ord(reaction.emoji)
        PEACH = 127825
        if emoji_code == PEACH:
            response, buttified = butt.buttify(message.clean_content)
            await message.channel.send(response)