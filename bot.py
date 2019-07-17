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

        if self.should_buttify():
            response = butt.buttify(message.content)
            await message.channel.send(response)

    def should_buttify(self):
        chance_to_butt = config.get_chance_to_butt()
        return random() <= chance_to_butt