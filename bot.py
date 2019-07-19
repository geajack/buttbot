from random import random

import discord

import config
import butt

class ButtBot(discord.Client):

    async def on_message(self, message):
        if self.is_visible(message):
            if self.should_buttify(message.clean_content):
                response, buttified = butt.buttify(message.clean_content)
                if buttified:
                    await message.channel.send(response)

    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        emoji_code = ord(reaction.emoji)
        PEACH = 127825
        if emoji_code == PEACH:
            response, buttified = butt.buttify(message.clean_content)
            await message.channel.send(response)

    def is_visible(self, message):
        server_id = message.guild.id
        channel_id = message.channel.id
        if not config.is_channel_authorized(server_id, channel_id):
            return False

        if message.author == self.user:
            return False

        return True

    def should_buttify(self, message):
        if config.contains_keyword(message):
            return True

        chance_to_butt = config.get_chance_to_butt()
        return random() <= chance_to_butt