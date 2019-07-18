from random import random

import discord

import config
import butt

class ButtBot(discord.Client):

    async def on_message(self, message):
        server_id = message.guild.id
        channel_id = message.channel.id
        if not config.is_channel_authorized(server_id, channel_id):
            return

        if message.author == self.user:
            return

        if self.should_buttify(message.clean_content):
            response = butt.buttify(message.clean_content)
            await message.channel.send(response)

    def should_buttify(self, message):
        if config.contains_keyword(message):
            return True

        chance_to_butt = config.get_chance_to_butt()
        return random() <= chance_to_butt